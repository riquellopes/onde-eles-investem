import scrapy
import json

from scrapy.http import Request
from scrapper.items import CandidatoItem


BASE_URL = "https://divulgacandcontas.tse.jus.br/divulga"
LISTA_CANDIDATOS = "/rest/v1/candidatura/listar/2020/60011/2030402020"
BUSCA_CANDIDATO = "/rest/v1/candidatura/buscar/2020/60011/2030402020"

class CandidatosSpider(scrapy.Spider):
    name = 'candidatos'
    allowed_domains = ['divulgacandcontas.tse.jus.br']
    start_urls = [
        f'{BASE_URL}{LISTA_CANDIDATOS}/11/candidatos',
        f'{BASE_URL}{LISTA_CANDIDATOS}/12/candidatos',
        f'{BASE_URL}{LISTA_CANDIDATOS}/13/candidatos'
    ]


    def parse_candidato(self, response):
        response_data = json.loads(response.text)

        yield CandidatoItem(dados=response_data)
        


    def parse(self, response):
        response_data = json.loads(response.text)

        for candidato in response_data['candidatos']:
            yield Request(f"{BASE_URL}{BUSCA_CANDIDATO}/candidato/{candidato['id']}", callback=self.parse_candidato)