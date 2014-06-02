# -*- coding:UTF-8 -*-

from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from sp1.items import Sp1Item
from scrapy.utils.response import get_base_url
from scrapy.utils.url import urljoin_rfc
#from scary import log

class Sp1Spider(BaseSpider):
	name = "fx168.com"
	start_urls = [
			#"http://www.fx168.com/forex/cad/1405/1013688.shtml"
			#"http://news.fx168.com/forex/",
			"http://news.fx168.com/bank/"
			]
	rootdir = '/tmp/spiderData/'

	def parse2(self, response):
		hxs = HtmlXPathSelector(response)
		item = response.meta['item']
		items = []
		contents = hxs.select('//p')

		for content in contents:
			desc = content.xpath('text()').extract()
			if desc:
				crnt_item = {} #contentItem()
				crnt_item['content'] = desc
				crnt_item['filenm'] = self.rootdir + response.url.split("/")[-2]+"_"+response.url.split("/")[-1]
				items.append(crnt_item)

		return items


	def parse(self, response):
		hxs = HtmlXPathSelector(response)
		items = []

		title = hxs.xpath('//a/text()').extract()
		url = hxs.xpath('//a/@href').extract()

		base_url = get_base_url(response)
		newurls = hxs.xpath('//a/@href').extract()
		validurls = []
		i=0
		for url in newurls:
			if True:#url[0]!='#' and url:
				#validurls.append(ural)
				item = Sp1Item()
				relative_url = urljoin_rfc(base_url,url)
				item['link'] = ralative_url
				item['title'] = title[i][:]
				validurls.append(relative_url)
			i = i+1

		#items.extend([self.make_requests_from_url(url).replace(callback=self.parse) for url in validurls])
		for url in validurls:
			yield Request(url['link'],meta = {'item':url,callback=self.parse2)


