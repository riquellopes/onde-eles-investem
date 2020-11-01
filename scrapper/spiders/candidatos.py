import scrapy


class CandidatosSpider(scrapy.Spider):
    name = 'candidatos'
    allowed_domains = ['https://divulgacandcontas.tse.jus.br/']
    start_urls = ['https://divulgacandcontas.tse.jus.br/divulga/rest/v1/']

    def parse(self, response):
        pass
