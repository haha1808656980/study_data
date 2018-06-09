# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import pymongo
import pymysql

class MovieprojectPipeline(object):
    def open_spider(self,spider):
        self.fp = open('movie.txt','w',encoding='utf8')

    def process_item(self, item, spider):
        d = dict(item)
        string = json.dumps(d,ensure_ascii=False)
        self.fp.write(string + '\n')
        return item

    def close_spider(self, spider):
        self.fp.close()
#存入到mongodb中
class MyMongoDbPipeline(object):
    def open_spider(self,spider):
        #连接数据库
        self.conn = pymongo.MongoClient(host='localhost',port=27017)
        #选择数据库，没有回自动创建
        db = self.conn.movie
        #选择集合
        self.collection = db.movie_collection

    def process_item(self, item, spider):
        self.collection.insert(dict(item))
        return item

    def close_spider(self, spider):
        self.conn.close()


from scrapy.utils.project import get_project_settings
class MyMySqlPipeline(object):
    def open_spider(self, spider):
        # 连接数据库
        settings = get_project_settings()
        host = settings['DB_HOST']
        port = settings['DB_PORT']
        user = settings['DB_USER']
        password = settings['DB_PASSWORD']
        dbname = settings['DB_NAME']
        dbcharset = settings['DB_CHARSET']
        self.conn = pymysql.Connect(host=host, port=port, user=user, password=password, db=dbname, charset=dbcharset)
        self.conn = pymysql.Connect(host=host, port=port, user=user, password=password, db=dbname, charset=dbcharset)

    def process_item(self, item, spider):
        # 写入数据库中
        sql = 'insert into movies(movie_poster, movie_name, movie_score, movie_type, movie_director, movie_screenwriter, movie_actor, movie_time, movie_content) values("%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s")'% (
        item['movie_poster'], item['movie_name'], item['movie_score'], item['movie_type'], item['movie_director'], item['movie_screenwriter'], item['movie_actor'],
        item['movie_time'], item['movie_content'])
        # 执行sql语句
        self.cursor = self.conn.cursor()
        try:
            self.cursor.execute(sql)
            self.conn.commit()
        except Exception as e:
            print(e)
            self.conn.rollback()
        return item

    def close_spider(self, spider):
        self.cursor.close()
        self.conn.close()
