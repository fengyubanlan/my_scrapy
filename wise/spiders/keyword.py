import scrapy

#爬取关键词为代运营的数据
class KeywordSpider(scrapy.Spider):
    name = 'keyword'
    allowed_domains = ['baidu.com']
    start_urls = ['https://www.baidu.com/s?wd=代运营']

    def parse(self, response):
        container = response.xpath('//*[@class="result c-container new-pmd"]')
        for div in container:
            print(div)
            print(div.xpath('div[@class="f13 c-gap-top-xsmall se_st_footer user-avatar"]/a[@class="c-showurl c-color-gray"]/text()').extract())
            id = div.xpath('@id').extract()[0] # div的id属性
            #// *[ @ id = "1"] / div[2]
