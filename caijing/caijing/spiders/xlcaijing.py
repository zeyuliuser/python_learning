# -*- coding: utf-8 -*-
import scrapy
from caijing.items import CaijingItem
from scrapy import cmdline

class XlcaijingSpider(scrapy.Spider):
    name = 'xlcaijing'
    # allowed_domains = ['http://vip.stock.finance.sina.com.cn']
    start_urls = ['http://vip.stock.finance.sina.com.cn/corp/go.php/vCB_Bulletin/stockid/600104/page_type/ndbg.phtml']
    article=[]


    def parse(self,response):
        # i = 0
        info_nums = response.xpath("//table[@class='table2']//ul//a/@href").extract()
        for info in info_nums:
            yield scrapy.Request(
                'http://vip.stock.finance.sina.com.cn' + info, callback=self.then)

    def then(self,response):
        # print(2000)
        # text = response.xpath("//pre").extract()
        articles = CaijingItem()
        articles['article'] = response.xpath("//pre").extract()
        # self.article.append(text)
        yield articles




