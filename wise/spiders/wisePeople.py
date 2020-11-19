import scrapy

from wise.items import WiseItem

#愚蠢的学习过程
class WisepeopleSpider(scrapy.Spider):
    name = 'wisePeople'
    allowed_domains = ['wise.xmu.edu.cn']
    start_urls = ['http://www.wise.xmu.edu.cn/people/faculty']

    def parse(self, response):
        tr_list = response.xpath('//tr[not(@class)]/td')
        count = 0
        item = WiseItem()
        for tr in tr_list:
            if count == 0:
                item = WiseItem()
            name = tr.xpath('normalize-space(text())').extract()[0]
            if name == '':
                a = tr.xpath('normalize-space(a[contains(@href,"/people/faculty/")]/text())').extract()
                if len(a)>0:
                    if a[0]!='':
                        print(a[0])
                        item['name'] = ''.join(a[0])
                        count+=1
            else:
                count += 1
                print(name)
                if count%2==0:
                    item['email'] = ''.join(name)
                else :
                    item['pro_title'] = ''.join(name)
            if count%3==0:
                count = 0
                yield item
