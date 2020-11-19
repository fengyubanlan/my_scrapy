# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from pymongo import MongoClient

from wise import settings

#保存数据的数据管道
class WisePipeline:
    def __init__(self):
        # 获取setting中主机名，端口号和集合名
        host = settings.MONGODB_HOST
        port = settings.MONGODB_PORT
        #dbname = settings.MONGODB_DBNAME
        #col = settings.MONGODB_COL

        # 创建一个mongo实例
        client = MongoClient(host=host, port=port)

        # 访问数据库
        #db = client[dbname]

        # 访问集合
        #self.col = db[col]

        # 访问数据连接器
        self.client = client

    def process_item(self, item, spider):
        data = dict(item)
        my_dbname = spider.dbname
        my_col = spider.col
        self.client[my_dbname][my_col].insert(data)
        #self.col.insert(data)
        return item
