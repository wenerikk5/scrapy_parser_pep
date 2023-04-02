import scrapy, re

from pep_parse.items import PepParseItem


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = ['peps.python.org']
    start_urls = ['https://peps.python.org/']
    flag = False

    def parse(self, response):
        main_tag = response.css('section#index-by-category')
        tbody_all = main_tag.css('tbody')
        tr_all = tbody_all.css("tr")

        if self.flag:
            self.flag = False
            yield PepParseItem({'number': 'Номер', 'name': 'Название', 'status': 'Статус' })

        for tr in tr_all:
            pep_url = tr.css('td a::attr(href)').get()
            yield response.follow(pep_url, callback=self.parse_pep)
    
    def parse_pep(self, response):

        title = response.css('h1.page-title::text').get()

        pattern = r'PEP\s(?P<number>\d+)\s[-–]+\s(?P<name>.*)'
        text_match = re.search(pattern, title)
        if text_match is not None:
            number, name = text_match.groups()
        else: 
            raise Exception(r'No match of Nubmer and Name in the PEP page {response.url}')

        status = response.css('dt:contains("Status") + dd abbr::text').get()
        data = {
            'number': number,
            'name': name,
            'status': status
        }
        yield PepParseItem(data)
