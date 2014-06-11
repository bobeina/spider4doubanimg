# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import codecs
import json

class Sp1Pipeline(object):
	def __init__(self):
		pass
	
	def process_item(self, item, spider):
		filename = item['filenm']
		self.file = codecs.open(filename, "a", encoding="utf-8")
		line = u"[title]\n%s\n[link]\n%s\n[img urls]\n%s\n[content]\n%s" % ( item['title'], item['link'], item['imgurls'], item['content'])
		self.file.write(line)
		self.file.close()
		return item
	
	#def spider_closed(self, spider):
	def close_spider(self, spider):
		pass



