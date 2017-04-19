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


class Spider(scrapy.Spider):
    name = "ami"
    allowed_domains = ["e-dictionary.apc.gov.tw"]
    download_delay = 0
    辭典網址 = 'http://e-dictionary.apc.gov.tw/{}/Search.htm'
    目錄網址 = 'http://e-dictionary.apc.gov.tw/{}/TermsMenu.htm'
    詞條網址 = 'http://e-dictionary.apc.gov.tw/{}/Term.htm'

    def __init__(self, lang='ami', ad=None, *args, **kwargs):
        super(Spider, self).__init__(*args, **kwargs)
        self.start_urls = [self.辭典網址.format(lang)]
        self.lang = lang

    def parse(self, response):
        for 目錄選項 in Selector(response).xpath(
            '//select[@id="ctl00_oCPH_Tabs_ddl_char"]/option'
        ):
            字首 = 目錄選項.xpath('text()').extract_first()
            編號 = 目錄選項.xpath('@value').extract_first()
            meta = {
                #                 'cookiejar': "%s_%d" % (self.lang, i),
                '字首': 字首,
                '目錄編號': 編號,
            }
            yield scrapy.FormRequest(
                self.目錄網址.format(self.lang, 編號),
                method='POST',
                formdata={'tsid': 編號},
                meta=meta, dont_filter=True,
                callback=self.掠目錄,
            )
            break

    def 掠目錄(self, response):
        self.logger.debug('掠 {} 的目錄'.format(response.meta['字首']))
        for 詞條選項 in Selector(response).xpath('//a[@class="w_term"]'):
            詞條編號 = 詞條選項.xpath('@rel').extract_first()
            詞條名 = 詞條選項.xpath('text()').extract_first()
            meta = {
                #                 'cookiejar': "%s_%d" % (self.lang, i),
                '詞條名': 詞條名,
            }
            yield scrapy.FormRequest(
                self.詞條網址.format(self.lang, 詞條編號),
                method='POST',
                formdata={'did': 詞條編號, 'fun': ''},
                meta=meta, dont_filter=True,
                callback=self.掠詞條,
            )
            break

    def 掠詞條(self, response):
        self.logger.debug('掠 {} 詞條'.format(response.meta['詞條名']))
        這詞條 = Selector(response)
        data = {'examples': []}
        data['name'] = 這詞條.xpath(
            '//div[@id="oGHC_Term"]/span/text()'
        ).extract_first()
        try:
            data['pronounce'] = urljoin(
                response.url,
                這詞條.xpath('//div[@id="oGHC_Term"]/a/@rel').extract_first()
            )
        except:
            data['pronounce'] = None
        data['frequency'] = ''.join(
            這詞條.xpath('//div[@id="oGHC_Freq"]/descendant::text()').extract()
        )

        try:
            data['source'] = (
                這詞條
                .xpath('//div[@id="oGHC_Source"]/a[@class="ws_term"]/text()').
                extract_first()
            )
        except:
            data['source'] = None
        descriptions = [''.join(x.xpath('descendant::text()').extract())
                        for x in 這詞條.xpath('//div[@class="block"]/div[1]')]
        sentences = [''.join(x.xpath('descendant::text()').extract()).strip()
                     for x in 這詞條.xpath('//div[@class="block"]/div[2]/table/tr[1]/td')]
        pronounces = [urljoin(response.url, x.extract()) for x in 這詞條.xpath(
            '//div[@class="block"]/div[2]/table/tr[1]/td/a[@class="play"]/@rel')]
        zh_Hants = [''.join(x.xpath('text()').extract()) for x in 這詞條.xpath(
            '//div[@class="block"]/div[2]/table/tr[2]/td')]
        for i in range(len(descriptions)):
            data['examples'].append({
                'description': descriptions[i],
                'sentence': sentences[i] if len(sentences) > i else None,
                'pronounce': pronounces[i] if len(pronounces) > i else None,
                'zh_Hant': zh_Hants[i] if len(zh_Hants) > i else None
            })
        return data
