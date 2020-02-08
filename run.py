from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from apscheduler.schedulers.twisted import TwistedScheduler
from tutorial.spiders.dejobs_spider import JobSpider

process = CrawlerProcess(get_project_settings())
scheduler = TwistedScheduler()
scheduler.add_job(process.crawl, 'cron', args=[JobSpider], hour = '11', minute='55')
scheduler.start()
process.start(False)
