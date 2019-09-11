# -*- coding: utf-8 -*-
import scrapy
from Tencet.items import TencetItem

class TencetSpider(scrapy.Spider):
	name = 'tencet'
	allowed_domains = ['tencent.com']
	#start_urls = ['http://tencent.com/']
	baseURL = "https://hr.tencent.com/position.php?&start="
	offset = 0
	start_urls = [baseURL + str(offset)]
	server = "https://hr.tencent.com/"


	def parse(self, response):
		node_list = response.xpath("//tr[@class = 'even'] | //tr[@class = 'odd']")
		for node in node_list:
			# 提取每个字段的信息，加入item中并转码
			item = TencetItem()
			item['positionName'] = node.xpath("./td[1]/a/text()").extract()[0]#.encode("utf-8")
			item['positionLink'] = node.xpath("./td[1]/a/@href").extract()[0]#.encode("utf-8")
			if len(node.xpath("./td[2]/text()")):
				item['positionType'] = node.xpath("./td[2]/text()").extract()[0]#.encode("utf-8")
			else:
				item['positionType'] = ""
			item['peopleNumber'] = node.xpath("./td[3]/text()").extract()[0]#.encode("utf-8")
			item['workLocation'] = node.xpath("./td[4]/text()").extract()[0]#.encode("utf-8")
			item['publishTime'] = node.xpath("./td[5]/text()").extract()[0]#.encode("utf-8")

			yield item
		# 适用于只能拼接url的情况,循环终点不确定
		#if(self.offset < 30):
		#	self.offset += 10
		#	url = self.baseURL + str(self.offset)
		#	# 下一页链接由callback值的方法来处理
		#	yield scrapy.Request(url,callback=self.parse)
		# 下一页用获取下一页链接来获取
		if not len(response.xpath("//a[@class = 'noactive' and @id = 'next']")):
			url = self.server+response.xpath("//a[@id='next']/@href").extract()[0]
			yield scrapy.Request(url, callback = self.parse)