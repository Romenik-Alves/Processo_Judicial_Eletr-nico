import scrapy
import pandas as pd

class ProjudiSpider(scrapy.Spider):
    name = "projudi"
    start_urls = ['https://projudi.tjam.jus.br/projudi/processo/consultaPublicaNova.do?actionType=iniciar']

    def parse(self, response):
        # Aqui você deve preencher os campos de pesquisa e enviar o formulário
        # Exemplo: 
        yield scrapy.FormRequest(
            url='https://projudi.tjam.jus.br/projudi/processo/consultaPublicaNova.do?actionType=iniciar',
            formdata={
                'foro': 'Todos',  # Altere conforme necessário
                'numero_processo': 'seu_numero_aqui',  # Substitua pelo número real
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

        # Adicione lógica para navegar por páginas, se necessário