import scrapy

class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    start_urls = [
        'http://quotes.toscrape.com/page/1/'
    ]

    def parse(self, response):
        print('*' * 10)
        print('\n\n')
        print(response.status, response.headers)
        print('*' * 10)
        print('\n\n')
