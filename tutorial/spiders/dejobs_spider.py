import scrapy
from scrapy.loader import ItemLoader
from tutorial.items import dejobsItem


class JobSpider(scrapy.Spider):
    name = "dejobs"
    allowed_domain = ["dejobs.org"]
    start_urls = ['https://dejobs.org/jobs/ajax/joblisting/?num_items=15&offset=']

    def parse(self, response):
        for i in range(0, 750, 15):
            yield response.follow('https://dejobs.org/jobs/ajax/joblisting/?num_items=15&offset=' + str(i), self.parse)

        urls = response.xpath("//li[@class='direct_joblisting with_description']/h4/a/@href").getall()
        for url in urls:
            page_url = 'https://dejobs.org' + url
            yield response.follow(page_url, self.parse_job)

    def parse_job(self, response):
        loader = ItemLoader(item=dejobsItem(), response=response)
        loader.add_value('url', response.url)
        loader.add_xpath('job_title', "//span[@class='direct_highlightedText']/span[1]/text()")
        loader.add_xpath('company_name', "//span[@class='direct_jobListingCompany']/span/text()")
        loader.add_xpath('job_description', "//div[@itemprop='description']//text()")
        loader.add_xpath('location', "//span[@class='direct_highlightedText']/span[2]/span/span[1]/text()")
        loader.add_xpath('country', "//span[@class='direct_highlightedText']/span[2]/span/span[2]/text()")
        loader.add_xpath('date_posted', "//div[@id='direct_listingDiv']/meta/@content")
        yield loader.load_item()

