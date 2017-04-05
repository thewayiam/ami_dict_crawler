# -*- coding: utf-8 -*-
from time import sleep
from random import randint
import re
from selenium.common.exceptions import TimeoutException
try:
    from urlparse import urljoin
except:
    from urllib.parse import urljoin
import scrapy
from scrapy.selector import Selector

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pyvirtualdisplay import Display


class Spider(scrapy.Spider):
    name = "ami"
    allowed_domains = ["e-dictionary.apc.gov.tw"]
    download_delay = 0

    def __init__(self, lang='ami', ad=None, *args, **kwargs):
        super(Spider, self).__init__(*args, **kwargs)
        self.display = Display(visible=0, size=(800, 600))
        self.display.start()
        self.driver = webdriver.Chrome("/var/chromedriver/chromedriver")
        self.start_urls = [
            "http://e-dictionary.apc.gov.tw/%s/Search.htm" % lang
        ]

    def click_to_word_list(self):
        li_terms = self.driver.find_element_by_xpath('//li[@id="li_terms"]/a')
        li_terms.click()
        try:
            WebDriverWait(self.driver, 100).until(
                EC.presence_of_element_located((By.ID, "oGHC_Term_Area"))
            )
        except:
            print('oGHC_Term_Area no found!!')
            sleep(randint(4, 5))

    def parse(self, response):
        self.driver.get(response.url)
        self.click_to_word_list()
        start_letters = self.driver.find_elements_by_xpath(
            '//select[@id="ctl00_oCPH_Tabs_ddl_char"]/option')
        for i, _start_letter in enumerate(start_letters):
            meta = {
                'cookiejar': "%s_%d" % ('ami', i),
                'start_letter': i
            }
            yield scrapy.Request(response.url, meta=meta, dont_filter=True, callback=self.parse_list)

    def parse_list(self, response):
        self.driver.get(response.url)
        self.click_to_word_list()

        previous_terms = None
        start_letters = self.driver.find_elements_by_xpath(
            '//select[@id="ctl00_oCPH_Tabs_ddl_char"]/option')
        for i, start_letter in enumerate(start_letters):
            if i != response.meta['start_letter']:
                continue
            previous_terms = self.driver.find_elements_by_xpath('//a[@class="w_term"]')
            start_letter.click()
            self.must_stale(previous_terms[0], start_letter.text)
            
            previous_name_element = None
            terms = self.driver.find_elements_by_xpath('//a[@class="w_term"]')
            for term in terms:
                term.click()
                try:
                    WebDriverWait(self.driver, 10).until(
                        EC.presence_of_element_located((By.XPATH, '//span[text()="%s"]' % term.text))
                    )
                except:
                    print(start_letter.text)
                    print(term.text)
                    sleep(randint(4, 5))
                    
                self.must_stale(
                    previous_name_element, start_letter.text + ' ' + term.text
                )
                data = {'examples': []}
                try:
                    previous_name_element = self.driver.find_element_by_xpath('//div[@id="oGHC_Term"]/span')
                    data['name'] = previous_name_element.text
                except Exception as err:
                    # pyu 的 ' 無資料
                    print('no name: %s' % term.text)
                    print(err)
                    continue
                try:
                    data['pronounce'] = urljoin(response.url, self.driver.find_element_by_xpath('//div[@id="oGHC_Term"]/a').get_attribute('rel'))
                except:
                    data['pronounce'] = None
                data['frequency'] = self.driver.find_element_by_xpath('//div[@id="oGHC_Freq"]').text
                try:
                    data['source'] = self.driver.find_element_by_xpath('//div[@id="oGHC_Source"]/a[@class="ws_term"]').text
                except:
                    data['source'] = None
                descriptions = [x.text for x in self.driver.find_elements_by_xpath('//div[@class="block"]/div[1]')]
                sentences = [x.text for x in self.driver.find_elements_by_xpath('//div[@class="block"]/div[2]/table/tbody/tr[1]/td')]
                pronounces = [urljoin(response.url, x.get_attribute('rel')) for x in self.driver.find_elements_by_xpath('//div[@class="block"]/div[2]/table/tbody/tr[1]/td/a[@class="play"]')]
                zh_Hants = [x.text for x in self.driver.find_elements_by_xpath('//div[@class="block"]/div[2]/table/tbody/tr[2]/td')]
                for i in range(len(descriptions)):
                    data['examples'].append({
                        'description': descriptions[i],
                        'sentence': sentences[i] if len(sentences) > i else None,
                        'pronounce': pronounces[i] if len(pronounces) > i else None,
                        'zh_Hant': zh_Hants[i] if len(zh_Hants) > i else None
                    })
                yield data

    def must_stale(self, previous_element, message):
        if previous_element is not None:
            try:
                WebDriverWait(self.driver, 20).until(
                    EC.staleness_of(previous_element)
                )
            except TimeoutException:
                print('%s did not update!!' % message)
        sleep(randint(1, 2))
