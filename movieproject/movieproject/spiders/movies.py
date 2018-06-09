# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from movieproject.items import MovieprojectItem
from scrapy_redis.spiders import RedisCrawlSpider

class MoviesSpider(RedisCrawlSpider):
    name = 'movies'
    allowed_domains = ['www.id97.com']
    redis_key = 'moviesspider:start_urls'

    #自己定制保存的数据库
    custom_settings = {
        'ITEM_PIPELINES':{
        'movieproject.pipelines.MyMongoDbPipeline': 301,
        # 'movieproject.pipelines.MyMySqlPipeline': 301,
        # 'scrapy_redis.pipelines.RedisPipeline': 400
        }
    }



    #匹配规则 在allow里面写入解析式
    page_link=LinkExtractor(allow=r'/movie/\?page=\d')
    #详情页
    detail_link = LinkExtractor(restrict_xpaths='//div[contains(@class,"col-xs-1-5")]/div/a')

    rules = (
        #处理页码，跟进处理
        Rule(page_link, follow=True),
        #处理详情页，不用跟进
        Rule(detail_link, callback='parse_item',follow=False),
    )

    def parse_item(self, response):

        item = MovieprojectItem()

        item['movie_poster'] =  response.xpath('//a[@class="movie-post"]/img/@src').extract_first()

        item['movie_name'] = response.xpath('//h1').xpath('string(.)').extract_first()

        item['movie_score'] = response.xpath('//div[@class="col-xs-8"]/table/tbody/tr[last()]/td[2]').xpath('string(.)').extract_first()

        item['movie_type'] = response.xpath('//div[@class="col-xs-8"]/table/tbody/tr[3]/td[2]').xpath('string(.)').extract_first()

        # 导演
        item['movie_director'] = response.xpath(
            '//div[@class="col-xs-8"]/table/tbody/tr[1]/td[2]/a/text()').extract_first()
        # 编剧
        item['movie_screenwriter'] = response.xpath('//div[@class="col-xs-8"]/table/tbody/tr[2]/td[2]/a/text()').extract_first()
        # 主演
        item['movie_actor'] = response.xpath('//div[@class="col-xs-8"]/table/tbody/tr[3]/td[2]').xpath(
            'string(.)').extract_first().replace(' ', '').replace('显示全部', '')
        # 片长
        lala = response.xpath('//div[@class="col-xs-8"]/table/tbody/tr[8]/td[2]/text()').extract_first()
        if lala and ('分钟' in lala):
            item['movie_time'] = lala
        else:
            item['movie_time'] = ''
        # 电影介绍
        introduce = response.xpath('//div[@class="col-xs-12 movie-introduce"]').xpath('string(.)').extract_first()
        if introduce == None:
            item['movie_content'] = ''
        else:
            item['movie_content'] = introduce.replace('\u3000', '').replace('展开全部', '')
        yield item