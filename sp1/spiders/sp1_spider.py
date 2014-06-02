# -*- coding:UTF-8 -*-

from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector,Selector
from sp1.items import Sp1Item
from scrapy.utils.response import get_base_url
from scrapy.utils.url import urljoin_rfc
#from scary import Selector

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
		#hxs = HtmlXPathSelector(response)
		hxs = Selector(response)
		items = []

		sites = hxs.xpath('//a') #hxs.xpath('//a/text()').extract()
		base_url = get_base_url(response)

		validurls = []
		i=0
		#for url in newurls:
		for site in sites:
			url = site.xpath('a/@href').extract()
			if self.name not in url:
				continue
			if url[0]=='/':#url[0]!='#' and url:
				#validurls.append(url)
				relative_url = urljoin_rfc(base_url,url)
			else:
				relative_url = url
			
			item = Sp1Item()
			item['link'] = relative_url
			#item['title'] = title[i][:]
			item['title'] =site.xpath('text()').extract()
			#validurls.append(relative_url)
			items.append(relative_url)

			print '\n\n\n---------------\ncrnt i = %d\n-------------\n\n\n'%i
			i = i+1

		#items.extend([self.make_requests_from_url(url).replace(callback=self.parse) for url in validurls])
		for url in validurls:
			yield Request(url['link'],meta = {'item':url},callback=self.parse2)


