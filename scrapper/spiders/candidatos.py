import scrapy
import json

from scrapper.items import CandidatoItem


class CandidatosSpider(scrapy.Spider):
    name = 'candidatos'
    allowed_domains = ['https://divulgacandcontas.tse.jus.br/']
    start_urls = ['https://divulgacandcontas.tse.jus.br/divulga/rest/v1/candidatura/listar/2020/60011/2030402020/11/candidatos']

    def parse(self, response):
        response_data = json.loads(response.text)

        for candidato in response_data['candidatos']:
            yield CandidatoItem(dados=candidato)