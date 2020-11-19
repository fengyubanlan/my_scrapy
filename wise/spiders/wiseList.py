import scrapy

from wise.items import WiseItem

#爬取测试的网站数据
class WiselistSpider(scrapy.Spider):
    name = 'wiseList'
    allowed_domains = ['wise.xmu.edu.cn']
    start_urls = ['http://www.wise.xmu.edu.cn/people/faculty']
    dbname = 'Wise'  #数据库名字
    col = 'wise_people'  #集合名字

    def parse(self, response):
        tr_list = response.xpath('//tr[not(@class)]')
        for tr in tr_list:
            item = WiseItem()
            name = tr.xpath('td/a/text()').extract()[0].strip() #名字
            pro_title = tr.xpath('td/text()').extract()[2].strip() #职称
            email = tr.xpath('td/text()').extract()[3].strip() #邮箱
            item['name'] = ''.join(name)
            item['pro_title'] = ''.join(pro_title)
            item['email'] = ''.join(email)
            yield item


