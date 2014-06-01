# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import codecs
import json

class Sp1Pipeline(object):
	def __init__(self):
		self.file = codecs.open("/tmp/out.json", "wb", encoding="utf-8")
	
	def process_item(self, item, spider):
		line = json.dumps(dict(item), ensure_ascii=False) + "\n"
		self.file.write(line)
		return item
	
	#def spider_closed(self, spider):
	def close_spider(self, spider):
		self.file.close()


'''
class Sp1Pipeline(object):
    def __init__(self):
	self.file = open('data.txt','wb')

    def process_item(self, item, spider):
	self.file.write(item['title'] + '\t' + item['link'] + '\t' + item['desc']+'\n')
        #return item
'''

