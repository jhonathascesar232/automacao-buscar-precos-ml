from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import os
import random
import schedule


def buscar_precos():
    #abrir o navergador
    driver = webdriver.Chrome(
        executable_path = os.getcwd() + os.sep + 'chromedriver.exe'
    )

    driver.get('https://www.mercadolivre.com.br/')
    sleep(random.randint(3,5))

    campo_pesquisa = driver.find_element_by_xpath(
        "//input[@class='nav-search-input']"
    )
    sleep(random.randint(3,5))

    campo_pesquisa.click()
    sleep(random.randint(3,5))

    #nome_produto = input('[*]\tDigite o nome do produto: ')

    campo_pesquisa.send_keys('fone hyperx')
    sleep(random.randint(3,5))

    campo_pesquisa.send_keys(Keys.ENTER)
    sleep(random.randint(3,5))

    while True:
        #extrair titulo e preco
        try:
            titulos = driver.find_elements_by_xpath(
                "//h2[@class='ui-search-item__title ui-search-item__group__element']"
            )
            sleep(random.randint(3,5))

        except:
            print("Não estamos no formato thumbnail!")

        try:
            titulos = driver.find_elements_by_xpath(
                "//h2[@class='ui-search-item__title"
            )
            sleep(random.randint(3,5))
        except:
            print("Não estamos no modo listagem!")

        precos = driver.find_elements_by_xpath(
            "//div[@class='ui-search-price ui-search-price--size-medium ui-search-item__group__element']//div[@class='ui-search-price__second-line']//span[@class='price-tag ui-search-price__part']//span[@class='price-tag-fraction']"
        )
        sleep(random.randint(3,5))

        for titulo, preco in zip(titulos,precos):
            with open('DADOS.txt', 'a', newline = '', encoding = 'utf-8') as arquivo:
                arquivo.write(titulo.text + ',' + preco.text + os.linesep)

        #navegar até a próxima página
        try:
            sleep(random.randint(3,5))
            driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
            botao_proximo = driver.find_element_by_xpath(
                "//li[@class='andes-pagination__button andes-pagination__button--next']"
            )
            sleep(random.randint(3,5))
            botao_proximo.click()
        except:
            pass

#agendamento
# schedule.every().thursday().at('07:00').do(buscar_precos)
# while True:
#     schedule.run_pending()
#     sleep(1)

buscar_precos()