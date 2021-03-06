# -*- coding:UTF-8 -*-
# sp1_spider.py

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
			#"http://www.douban.com/group/haixiuzu",
			"http://www.douban.com/group/meituikong"
			]
	rootdir = '/tmp/spiderData/'
        allowed_domains = ['douban.com']


        def parse(self, response):
		#item = Sp1Item()
		hxs         = HtmlXPathSelector(response)
		raw_urls  = hxs.select("//a/@href").extract()
		urls      = []
		
		pattern_topic = re.compile(r'http://www.douban.com/group/topic/(\d+)/')
		pattern_topic_list = re.compile(r'http://www.douban.com/group/(\w+)/discussion\?start=(\d+)')
		for url in raw_urls:
			match_list = pattern_topic_list.match(url)
			match_topic = pattern_topic.match(url)
			if match_list or match_topic:
				urls.append(url)
		
		for url in urls:
			yield Request(url,meta = {'item':url},callback=self.parse)
			
		# get img
		match_crnt_topic = pattern_topic.match(response.url)
		topic = hxs.xpath('//div/h1/text()').extract()
		
		if match_crnt_topic:
			imgurls = hxs.xpath("//div[@class='topic-figure cc']/img/@src").extract()
			if imgurls:
				contents = hxs.xpath('//p/text()').extract()
				desc = '\n'.join(contents)
				imgurls = hxs.xpath("//div[@class='topic-figure cc']/img/@src").extract()
				imgurls_txt = ''
				
				imgurls_txt = ';'.join(imgurls)
				crnt_item = Sp1Item()
				crnt_item['title'] = topic[0]
				crnt_item['filenm'] = self.rootdir + response.url.split("/")[-2]+"_"+response.url.split("/")[-1]
				crnt_item['link'] = response.url
				crnt_item['content'] = desc
				crnt_item['imgurls'] = imgurls_txt
				yield crnt_item

