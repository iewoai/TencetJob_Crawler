# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json,os,csv
from scrapy.exporters import XmlItemExporter
#class MyEncoder(json.JSONEncoder):
		#def default(self, obj):
		#只要检查到了是bytes类型的数据就把它转为str类型
		#:param obj:
		#:return:
		#	if isinstance(obj, bytes):
		#		return str(obj, encoding='utf-8')
		#	return json.JSONEncoder.default(self, obj)
class TencetPipeline(object):
		def __init__(self):
			#将item写入csv文件
			#self.f = open("tencet.csv","w",newline="")
			#filenames = ['positionName','positionLink','positionType','peopleNumber','workLocation','publishTime']
			#self.writer = csv.DictWriter(self.f,fieldnames = filenames)
			
			#将item写入txt文件
			self.f = open("tencet0.text","w")

			#将item写入json文件
			#self.f = open("tencet1.json","w")
			
			#self.file = open("tencet.csv", "w")  # lagoudata13.csv为将要写入的文件名
			#self.exporter = CsvItemExporter(self.file,fields_to_export=['positionName','positionLink','positionType','peopleNumber','workLocation','publishTime']) # fields_to_export 为Items字段列表
			#self.exporter.start_exporting()

		def process_item(self, item, spider):
			#写入txt文件
			line = str(dict(item)) + ',\n'
			self.f.write(line)

			#写入json文件
			#content = json.dumps(dict(item), ensure_ascii = False) + ",\n"
			#self.f.write(content)
			
			#写入csv文件
			#item = dict(item)
			#self.writer.writerow({item['positionName'],item['positionLink'],item['positionType'],item['peopleNumber'],item['workLocation'],item['publishTime']})
			#self.exporter.export_item(item)
			return item

		def close_spider(self, spider):
			self.exporter.finish_exporting()
			self.f.close()
