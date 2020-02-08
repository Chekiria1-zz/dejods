# -*- coding: utf-8 -*-
from scrapy.item import Item, Field
from scrapy.loader.processors import TakeFirst, Join


class dejobsItem(Item):
    crawled_date = Field(output_processor=TakeFirst())
    url = Field(output_processor=TakeFirst())
    job_title = Field(output_processor=TakeFirst())
    company_name = Field(output_processor=TakeFirst())
    location = Field(output_processor=TakeFirst())
    job_url = Field(output_processor=TakeFirst())
    job_description = Field(output_processor=Join())
    country = Field(output_processor=TakeFirst())
    date_posted = Field(output_processor=TakeFirst())


