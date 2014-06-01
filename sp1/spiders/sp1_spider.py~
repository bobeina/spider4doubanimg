# -*- coding:UTF-8 -*-

from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from sp1.items import Sp1Item

class Sp1Spider(BaseSpider):
	name = "fx168.com"
	start_urls = [
			"http://www.fx168.com/forex/cad/1405/1013688.shtml"
			#"http://news.fx168.com/forex/",
			#"http://news.fx168.com/bank/"
			]

	def parse(self, response):
		#filenm = response.url.split("/")[-2]
		#open(filenm, 'wb').write(response.body)
		hxs = HtmlXPathSelector(response)
		#sites = hxs.select('//ul/li')
		sites = hxs.select('//p')
		items = []
		for site in sites:
			item = Sp1Item()
			item['title']= site.select('a/text()').extract()
			item['link']= site.select('a/@href').extract()
			item['desc']= site.select('text()').extract()
			items.append(item)
		return items



