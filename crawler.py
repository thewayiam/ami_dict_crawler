# -*- coding: utf-8 -*-
from time import sleep
from random import randint
import codecs
import re
import urllib
import urllib2
from urlparse import urljoin
import scrapy
from scrapy.http import Request, FormRequest
from scrapy.selector import Selector

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pyvirtualdisplay import Display


class Spider(scrapy.Spider):
    name = "ami"
    allowed_domains = ["e-dictionary.apc.gov.tw"]
    start_urls = [
        "http://e-dictionary.apc.gov.tw/ami/Search.htm",
    ]
    download_delay = 0

    def __init__(self, ad=None, *args, **kwargs):
        super(Spider, self).__init__(*args, **kwargs)
        self.display = Display(visible=0, size=(800, 600))
        self.display.start()
        self.driver = webdriver.Chrome("/var/chromedriver/chromedriver")

    def parse(self, response):
        self.driver.get(response.url)
        li_terms = self.driver.find_element_by_xpath('//li[@id="li_terms"]/a')
        li_terms.click()
        sleep(randint(1, 2))
#       with codecs.open("log/terms.htm", "w", encoding="utf-8") as f:
#           f.write(self.driver.page_source)
        start_letters = self.driver.find_elements_by_xpath('//select[@id="ctl00_oCPH_Tabs_ddl_char"]/option')
        for i, start_letter in enumerate(start_letters):
            start_letter.click()
            try:
                element = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((By.ID, "oGHC_Term_Area"))
                )
            except:
                print start_letter.text
                continue
            sleep(randint(1, 2))
            terms = self.driver.find_elements_by_xpath('//a[@class="w_term"]')
            for i, term in enumerate(terms):
                term.click()
                try:
                    element = WebDriverWait(self.driver, 10).until(
                        EC.presence_of_element_located((By.XPATH, '//span[text()="%s"]' % term.text))
                    )
                except:
                    print start_letter.text
                    print term.text
                    continue
                sleep(randint(1, 2))
                data = {'examples': []}
                data['name'] = self.driver.find_element_by_xpath('//div[@id="oGHC_Term"]/span').text
                try:
                    data['pronounce'] = urljoin(response.url, self.driver.find_element_by_xpath('//div[@id="oGHC_Term"]/a').get_attribute('rel'))
                except:
                    data['pronounce'] = None
                data['frequency'] = self.driver.find_element_by_xpath('//div[@id="oGHC_Freq"]').text
                try:
                    data['source'] = self.driver.find_element_by_xpath('//div[@id="oGHC_Source"]/a[@class="ws_term"]').text
                except:
                    data['source'] = None
                examples = self.driver.find_elements_by_xpath('//div[@class="concon"]/div')
                descriptions = [x.text for x in self.driver.find_elements_by_xpath('//div[@class="block"]/div[1]')]
                sentences = [x.text for x in self.driver.find_elements_by_xpath('//div[@class="block"]/div[2]/table/tbody/tr[1]/td')]
                pronounces = [urljoin(response.url, x.get_attribute('rel')) for x in self.driver.find_elements_by_xpath('//div[@class="block"]/div[2]/table/tbody/tr[1]/td/a')]
                zh_Hants = [x.text for x in self.driver.find_elements_by_xpath('//div[@class="block"]/div[2]/table/tbody/tr[2]/td')]
                for i in range(len(descriptions)):
                    data['examples'].append({
                        'description': descriptions[i],
                        'sentence': sentences[i] if len(sentences) > i else None,
                        'pronounce': pronounces[i] if len(pronounces) > i else None,
                        'zh_Hant': zh_Hants[i] if len(zh_Hants) > i else None
                    })
                yield data
#           with codecs.open("log/%s.htm" % start_letter.text, "w", encoding="utf-8") as f:
#               f.write(self.driver.page_source)
