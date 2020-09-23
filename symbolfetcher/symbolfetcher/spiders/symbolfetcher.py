import scrapy
#scrapy crawl symbolscrape -o quotes.jl

class ToScrapeSpiderXPath(scrapy.Spider):
    name = 'symbolscrape'
    start_urls = [
        'https://old.nasdaq.com/screening/companies-by-name.aspx?letter=0&exchange=nasdaq',
    ]

    def parse(self, response):
        names = response.xpath('//form[@method="post"]//table[@id="CompanylistResults"]//h3/a/text()').getall()
        for symbol in names:
            yield {
                'symbol': symbol[20:]
            }
        next_page_url = response.xpath('//li/a[@id="two_column_main_content_lb_NextPage"]@href').extract_first()
        if next_page_url is not None:
            yield scrapy.Request(response.urljoin(next_page_url))
'''