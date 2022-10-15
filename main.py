import scrapy  

class AluraBot(scrapy.Spider):
    name = "Bot Alura"
    start_urls =["https://www.alura.com.br/cursos-online-programacao"]
    
    def parse(self, response):
        SELETOR = ".subcategoria__item"
        cursos = []

        for categoria in response.css(SELETOR):
            curso = {}

            NOME_SELETOR = ".card-curso__nome ::text"
            LINK_SELECTOR = ".card-curso ::attr(href)"

            curso ['nome'] = categoria.css (NOME_SELETOR)
            curso ['link'] = "https://www.alura.com.br" + categoria.css(LINK_SELECTOR)

            print(curso)
            cursos.append(curso)

        print("Total de Cursos:", len(cursos))
        
        
        """ execução = scrapy runspider + nome do arquivo .py"""