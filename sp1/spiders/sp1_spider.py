# -*- coding:UTF-8 -*-

from scrapy.spider import BaseSpider,Spider
from scrapy.selector import HtmlXPathSelector,Selector
from sp1.items import Sp1Item
from scrapy.utils.response import get_base_url
from scrapy.utils.url import urljoin_rfc
from scrapy.http import Request

class Sp1Spider(Spider):#(BaseSpider):
	name = "douban.com" #"fx168.com"
	start_urls = [
			#"http://www.fx168.com/forex/cad/1405/1013688.shtml"
			#"http://news.fx168.com/forex/",
			#"http://news.fx168.com/bank/"
			"http://www.douban.com"
			]
	rootdir = '/tmp/spiderData/'

	def parse2(self, response):
		hxs = HtmlXPathSelector(response)
		item = response.meta['item']
		items = []
		contents = hxs.select('//p')

		for content in contents:
			desc = content.xpath('text()').extract()
			if True:#desc:
				crnt_item = Sp1Item() #contentItem()
				crnt_item['content'] = desc
				crnt_item['filenm'] = self.rootdir + response.url.split("/")[-2]+"_"+response.url.split("/")[-1]
				items.append(crnt_item)

		return items


	def parse(self, response):
		hxs = Selector(response)
		items = []

		sites = hxs.xpath('//a') #hxs.xpath('//a/text()').extract()
		base_url = get_base_url(response)

		validurls = []
		#i=0

		for site in sites:
			url = site.select('@href').extract()
			#print '        <<<',url,'>>>'
			if url[0]:
				if url[0][0]=='#':
					continue
				if url[0][0]=='/':
					relative_url = urljoin_rfc(base_url,url[0])
					#print '----------------------',relative_url[0]
				else:
					relative_url = url[0]
			else:
				continue
			
			item = Sp1Item()
			item['link'] = relative_url
			item['title'] =site.select('text()').extract()
			validurls.append(item)
			#i = i+1

		for crntlink in validurls:
			#print " ############################ link=",crntlink['link'],'#############################'

			try:
				yield Request(crntlink['link'],meta = {'item':crntlink},callback=self.parse2)
			except:
				pass


