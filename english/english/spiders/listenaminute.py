import scrapy

from scrapy.spiders import CrawlSpider
from ..items import EnglishItem



"""xpath
#ABC:  /html/body/div[2]/table/tbody/tr[1]/td
all ABC /html/body/div[2]/table/tbody/tr[@class=\"abc\"]/td
//tr[@class=\"abc\"]/td
//tr/td[@class=\"abc\"]
//tr/td/a"]
"""
class listenaminute(CrawlSpider):
    name = 'listenaminute'
    allowed_domains = ['listenaminute.com/']
    start_urls = ['https://listenaminute.com',]
    # https://listenaminute.com/a/accidents.html

    def parse(self, response):
        # headers = scrapy.Selector(response).xpath("//tr[@class=\"abc\"]/td/text()")
        # item = EnglishItem()
        # tmp_data = []
        # for header in headers:
        #     tmp_data.append(header.extract())

        # headers_2 = scrapy.Selector(response).xpath("//tr/td[@class=\"abc\"]/text()")
        # for header in headers_2:
        #     tmp_data.append(header.extract())

        # item['prefix']= tmp_data
        # yield item

        # /html/body/div[2]/table/tbody/tr[2]/td[1]/a
        item = EnglishItem()
        words = scrapy.Selector(response).xpath("//tr/td/a/text()").extract()
        # words.getall()
        # print("hanhmh1203___ of {0}".format((words)))
        tmp_words = []
        i=0
        for word in enumerate(words):
            tmp_word= {}
            # print("word_____ i = {0} value: {1}".format(i, word))
            # try:
            #     print("word_____ i = {0} value: {1}".format(i,(word.xpath('@href').get())))
            # except:
            #     print("An exception occurred")

            

            # break
            # print("link_____ i = {} value: {1} ".format(i,( word.xpath("//a[@href]/@href").extract())))
            
            # tmp_word['original'] = word.extract()

            tmp_word['word'] = word
            # tmp_word['link_____'] = word.xpath("@href").get()

            # tmp_word['original'] ='original'
            # tmp_word['word'] = 'word'
            # tmp_word['link'] = 'link'

            # break
            # tmp_word['link'] = word.xpath.text.extract
            
            # print("tmp_words____ i = {0} value: {1}".format(i, tmp_words[i]))
            tmp_words.append(word)
            # i = i +1
            # if i==3: 
            #     break
        item['idword'] = 1
        item['word_text'] = 'tmp_words'
        yield item