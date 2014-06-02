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

	def parse(self, response):
		'''
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
			item['filenm']=response.url.split("/")[-2]+"_"+response.url.split("/")[-1]
			items.append(item)
		return items
		'''
		hxs = HtmlXPathSelector(response)
		items = []

		#newurls = hxs.select('//a/@href').extract()
		base_url = get_base_url(response)
		newurls = hxs.xpath('//a/@href').extract()
		validurls = []
		for url in newurls:
			if True:#url[0]!='#' and url:
				#validurls.append(url)
				relative_url = urljoin_rfc(base_url,url)
				validurls.append(relative_url)

		#items.extend([self.make_requests_from_url(url).replace(callback=self.parse) for url in validurls])
		for url in validurls:
			yield Request(url,meta = {'item':url},callback=)

		sites = hxs.select('//p')
		items = []
		rootdir = '/tmp/spiderData/'
		for site in sites:
			desc = site.select('text()').extract()
			if desc:
				item = Sp1Item()
				item['title'] = site.select('a/text()').extract()
				item['link'] = site.select('a/@href').extract()
				item['desc'] = desc #site.select('text()').extract()
				item['filenm'] = rootdir + response.url.split("/")[-2]+"_"+response.url.split("/")[-1]
				items.append(item)
		return items



