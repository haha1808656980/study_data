# -*- coding: utf-8 -*-
import scrapy
from movieproject.items import MovieprojectItem

class MovieSpider(scrapy.Spider):
    name = 'movie'
    allowed_domains = ['www.id97.com']
    start_urls = ['http://www.id97.com/movie/']

    def parse(self, response):
        list_div = response.xpath('//div[contains(@class,"col-xs-1-5")]')
        for div in list_div:
            item = MovieprojectItem()

            item['movie_poster']=div.xpath('.//img/@data-original').extract_first()

            item['movie_name'] = div.xpath('.//img/@alt').extract_first()

            item['movie_score'] = div.xpath('.//div[@class="meta"]/h1/em/text()').extract_first().strip('- ')

            item['movie_type'] = div.xpath('.//div[@class="otherinfo"]').xpath('string(.)').extract_first()

            item['movie_url'] = div.xpath('.//div[@class="movie-item-in"]/a/@href').extract_first()

            yield item

            yield scrapy.Request(url=item['movie_url'],callback=self.parse_detail,meta={'item':item})

        

    def parse_detail(self,response):
        item = response.meta['item']

        item['movie_director'] = response.xpath('//table/tbody/tr[1]/td[2]/a/text()').extract_first()

        item['movie_screenwriter'] = response.xpath('//table/tbody/tr[2]/td[2]').xpath('string(.)').extract_first().replace(' ','')

        item['movie_actor'] = response.xpath('//table/tbody/tr[3]/td[2]').xpath('string(.)').extract_first().replace(' ','').replace('显示全部','')

        item['movie_country'] = response.xpath('//table/tbody/tr[5]/td[2]/a/text()').extract_first()

        item['show_time'] = response.xpath('//table/tbody/tr[7]/td[2]/text()').extract_first()

        item['movie_time'] = response.xpath('//table/tbody/tr[8]/td[2]/text()').extract_first()

        item['movie_content'] = response.xpath('//div[@class="col-xs-12 movie-introduce"]/p/text()').extract_first().strip('\u3000')
        yield item