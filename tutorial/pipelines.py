# -*- coding: utf-8 -*-
import json
from sqlalchemy.orm import sessionmaker
from tutorial.models import dejobsbase, db_connect, create_table
import logging
from time import gmtime, strftime

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class TutorialPipeline(object):
    def process_item(self, item, spider):
        return item

class JsonPipeline(object):
    def open_spider(self, spider):
        self.file = open('de_jobs {}.json'.format(strftime("%Y-%m-%d %H_%M_%S", gmtime())), 'w')

    def close_spider(self, spider):
        self.file.close()

    def process_item(self, item, spider):
        line = json.dumps(dict(item)) + "\n"
        self.file.write(line)
        return item


class CsvPipeline(object):
    def open_spider(self, spider):
        self.file = open('de_jobs {}.csv'.format(strftime("%Y-%m-%d %H_%M_%S", gmtime())), 'w')

    def close_spider(self, spider):
        self.file.close()

    def process_item(self, item, spider):
        self.file.write(str(item))
        return item


class SaveQuotesPipeline(object):
    def __init__(self):
        """
        Initializes database connection and sessionmaker
        Creates tables
        """
        engine = db_connect()
        create_table(engine)
        self.Session = sessionmaker(bind=engine)
        logging.info("****SaveQuotePipeline: database connected****")

    def process_item(self, item, spider):
        """Save quotes in the database
        This method is called for every item pipeline component
        """
        session = self.Session()
        dejobs = dejobsbase()
        dejobs.url = item["url"]
        dejobs.job_title = item["job_title"]
        dejobs.company_name = item["company_name"]
        dejobs.job_description = item["job_description"]
        dejobs.location = item["location"]
        dejobs.country = item["country"]
        dejobs.date_posted = item["date_posted"]

        try:
            session.add(dejobs)
            session.commit()

        except:
            session.rollback()
            raise

        finally:
            session.close()

        return item
