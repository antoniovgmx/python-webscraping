import os
from selenium import webdriver
from selenium.webdriver import Chrome #https://www.selenium.dev/documentation/en/webdriver/driver_requirements/ && https://sites.google.com/a/chromium.org/chromedriver/downloads
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.support.ui import WebDriverWait #https://www.selenium.dev/documentation/en/webdriver/waits/
from selenium.webdriver.common.by import By #https://www.selenium.dev/documentation/en/webdriver/web_element/
from selenium.webdriver.common.keys import Keys
import time


def findMicrosoft(search_param):

    chrome_options = webdriver.ChromeOptions()
    chrome_options.headless = True
    chrome_options.add_argument('ignore-certificate-errors')
    chrome_options.add_argument('--ignore-ssl-errors')
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36")

    chrome_path = os.path.abspath("../usr/lib/chromium-browser/chromedriver")
    driver = webdriver.Chrome(chrome_path, chrome_options=chrome_options)

    url = 'https://academic.microsoft.com/search?q={}%20'.format(search_param)
    driver.get(url)
    # print("entro a la pagina")
    articlesData = []
    time.sleep(5)
    if (len(driver.find_elements_by_class_name("author-card")) == 0 ):
        driver.close()
        return ("ERROR : NO SE ENCONTRARON ARTICULOS")
    else:
        pass
    search = driver.find_element_by_class_name("author-card")
    # print("found autor-card")
    search = search.find_element_by_class_name("header")
    search = search.find_element_by_xpath("//div[@class='name']/a").get_attribute('href')
    driver.get(search)
    time.sleep(4)

    while True:
        articles = driver.find_elements_by_class_name("primary_paper")

        for article in articles:
            title = article.find_element_by_class_name("au-target").text
            date =  article.find_element_by_class_name("year").get_attribute('textContent')
            authors_div = article.find_elements_by_class_name("author")
            authors = []
            for author in authors_div:
                authors.append(author.get_attribute('innerText'))

            data = {
                "title" : title,
                "date" : date,
                # "DOI" : DOI,
                # "ISBN" : ISBN,
                "collaborators" : authors
            }

            # Agregamos el artículo a la lista
            articlesData.append(data)

        try:
            button = driver.find_element_by_xpath("//i[@class='icon-up right au-target']")
            button.click()
            time.sleep(3)
        except:
            microsoftData = {
                "articles" : articlesData,
                "Microsoft count" : len(articlesData)
            }
            driver.close()
            return microsoftData