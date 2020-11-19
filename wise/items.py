# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

#保存数据的item
class WiseItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    name = scrapy.Field() #名字

    pro_title = scrapy.Field() #职称

    email = scrapy.Field() #邮箱

class ApeItem(scrapy.Item):

    province_name = scrapy.Field()  # 省份名字

    province_code = scrapy.Field()  # 省份编码

    city_name = scrapy.Field()  # 地市名字

    city_code = scrapy.Field()  # 地市编码

    city_id = scrapy.Field()  # city_id



