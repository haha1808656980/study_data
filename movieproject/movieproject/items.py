# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MovieprojectItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #电影海报
    movie_poster = scrapy.Field()
    #电影名字
    movie_name = scrapy.Field()
    #电影评分
    movie_score = scrapy.Field()
    #电影类型
    movie_type = scrapy.Field()

    #电影导演
    movie_director = scrapy.Field()
    #编剧
    movie_screenwriter = scrapy.Field()
    #演员
    movie_actor = scrapy.Field()
    #时长
    movie_time = scrapy.Field()
    #电影内容
    movie_content = scrapy.Field()


