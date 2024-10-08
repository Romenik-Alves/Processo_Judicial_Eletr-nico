import scrapy
import pandas as pd

class PjeSpider(scrapy.Spider):
    name = "pje"
    start_urls = ['https://pje1g.trf1.jus.br/pje/login.seam/']

    def parse(self, response):
        # Preencher campos de pesquisa e enviar formulário
        yield scrapy.FormRequest(
            url='https://pje1g.trf1.jus.br/pje/login.seam/',
            formdata={
                'campo1': 'valor1',  # Altere conforme necessário
                # Adicione outros campos se necessário
            },
            callback=self.parse_results
        )

    def parse_results(self, response):
        # Extraia os dados desejados
        for item in response.css('div.classe-do-item'):  # Altere a classe conforme necessário
            yield {
                'titulo': item.css('h2::text').get(),
                'imagem': item.css('img::attr(src)').get(),
                # Adicione mais campos conforme necessário
            }