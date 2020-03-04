# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class EnglishItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # prefix = scrapy.Field()
    idword = scrapy.Field()
    word_text = scrapy.Field()
    link = scrapy.Field()

