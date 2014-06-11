# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import codecs
import json

class Sp1Pipeline(object):
	def __init__(self):
		#self.file = codecs.open("/tmp/out.json", "wb", encoding="utf-8")
		#filename = response.url.split("/")[-2]
		#self.file = codecs.open(filename, "wb", encoding="utf-8")
		pass
	
	def process_item(self, item, spider):
		filename = item['filenm']
		self.file = codecs.open(filename, "a", encoding="utf-8")
		#line = json.dumps(dict(item))#, ensure_ascii=False)# + "\n"
		line = u"[title]\n%s\n[filename]\n%s\n[link]\n%s[content]\n%s" % ( item['title'], item['filenm'], item['link'], item['content'])
		self.file.write(line)
		self.file.close()
		return item
	
	#def spider_closed(self, spider):
	def close_spider(self, spider):
		#self.file.close()
		pass


'''
class Sp1Pipeline(object):
    def __init__(self):
	self.file = open('data.txt','wb')

    def process_item(self, item, spider):
	self.file.write(item['title'] + '\t' + item['link'] + '\t' + item['desc']+'\n')
        #return item
'''

