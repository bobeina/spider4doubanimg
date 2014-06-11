# -*- coding:UTF-8 -*-

from scrapy.spider import BaseSpider,Spider
from scrapy.selector import HtmlXPathSelector,Selector
from sp1.items import Sp1Item
from scrapy.utils.response import get_base_url
from scrapy.utils.url import urljoin_rfc
from scrapy.http import Request

import re

class Sp1Spider(Spider):#(BaseSpider):
	name = "douban.com" #"fx168.com"
	start_urls = [
			#"http://www.fx168.com/forex/cad/1405/1013688.shtml"
			#"http://news.fx168.com/forex/",
			#"http://news.fx168.com/bank/"
			#"http://www.douban.com/group/explore"
			#"http://www.douban.com/"
			#"http://www.douban.com/group/haixiuzu",
			"http://www.douban.com/group/meituikong"
			]
	rootdir = '/tmp/spiderData/'

        allowed_domains = ['douban.com']

	'''
        rules = (
            #Rule(SgmlLinkExtractor(allow=(r'http://www.qunar.com/routes/.*')), callback='parse'),
            #Rule(SgmlLinkExtractor(allow=('http:.*/routes/.*')), callback='parse'),
        )
	'''

        def parse(self, response):
		#item = Sp1Item()
		hxs         = HtmlXPathSelector(response)
		raw_urls  = hxs.select("//a/@href").extract()
		urls      = []
		
		pattern_topic = re.compile(r'http://www.douban.com/group/topic/(\d+)/')
		pattern_topic_list = re.compile(r'http://www.douban.com/group/(\w+)/discussion\?start=(\d+)')
		for url in raw_urls:
			#print '=================> url = ',url
			match_list = pattern_topic_list.match(url)
			match_topic = pattern_topic.match(url)
			if match_list or match_topic:
				urls.append(url)
		
		for url in urls:
			#yield Request(url)
			yield Request(url,meta = {'item':url},callback=self.parse)
			
		# get img
		match_crnt_topic = pattern_topic.match(response.url)
		topic = hxs.xpath('//div/h1/text()').extract()
		
		if match_crnt_topic:
			contents = hxs.xpath('//p/text()').extract()
			desc = ''
			for content in  contents:
				desc = desc.join(content)
				desc = desc.join("\n")
			crnt_item = Sp1Item()
			crnt_item['title'] = topic[0]
			crnt_item['filenm'] = self.rootdir + response.url.split("/")[-2]+"_"+response.url.split("/")[-1]
			crnt_item['link'] = response.url
			crnt_item['content'] = desc
			#item.append(crnt_item)
			yield crnt_item

        '''
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

		topic_url = 'topic'
		i = 0
		for site in sites:
			if i>2:
				break

			url = site.xpath('@href').extract()
			#print '        <<<',url,'>>>'
			if url[0]:
				if url[0][0]=='#':
					continue
				if url[0][0]=='/' or url[0][0]=='?' :
					relative_url = urljoin_rfc(base_url,url[0])
					#print '----------------------',relative_url[0]
				else:
					relative_url = url[0]
			else:
				continue

			if topic_url not in relative_url:
				#print u'~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~%s'%(relative_url)
				continue
			
			item = Sp1Item()
			item['link'] = relative_url
			item['title'] =site.xpath('text()').extract()
			validurls.append(item)
			i = i+1

		for crntlink in validurls:
			yield Request(crntlink['link'],meta = {'item':crntlink},callback=self.parse)
			yield Request(crntlink['link'],meta = {'item':crntlink},callback=self.parse2)
	'''


