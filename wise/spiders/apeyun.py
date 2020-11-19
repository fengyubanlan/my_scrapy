import json

import scrapy

from wise.items import ApeItem

#爬取apeyun的city数据
class ApeyunSpider(scrapy.Spider):
    name = 'apeyun'
    allowed_domains = ['apeyun.com']
    start_urls = ['https://www.apeyun.com/v1/index/get-city?token=6aed9feeade16f2fcee52dd084d62c23&t=1605598574000']
    dbname = 'Wise' #数据库名字
    col = 'ape_city_data'  #集合名字

    def parse(self, response):
        #print(response.body)
        source = json.loads(response.body)
        #print(source)
        district = source.get('data').get('district')
        #print(district)
        for dis in district:
            province_name = dis.get('name')
            child_list = dis.get('child')
            for child in child_list:
                name = child.get('name')
                city_id = child.get('city_id')
                province = child.get('province')
                city = child.get('city')
                item = ApeItem()
                item['city_id'] = ''.join(city_id)
                item['province_name'] = ''.join(province_name)
                item['province_code'] = ''.join(str(province))
                item['city_name'] = ''.join(name)
                item['city_code'] = ''.join(str(city))
                yield item
        #print(response.xpath('@data').extract())
