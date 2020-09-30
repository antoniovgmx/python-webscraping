from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

page_counter = 0
last_page = ''

driver = webdriver.Chrome()

driver.get("https://www.researchgate.net/")
print(driver.title)

search = driver.find_element_by_class_name("index-search-field__input")
search.send_keys('"escudero-nahon"')
search.send_keys(Keys.RETURN)

try:
    content = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "search__content"))
        )

    pages = content.find_elements_by_class_name('nova-c-button-group__item')
    last_page = pages[-2].text

finally:
    pass

while page_counter < int(last_page):
    try:
        content = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "search__content"))
        )
        
        articles = content.find_elements_by_xpath('//div[@class="nova-o-stack__item"]')
        for article in articles:
            try:
                headline = article.find_elements_by_xpath('.//div[@class="nova-e-text nova-e-text--size-l nova-e-text--family-sans-serif nova-e-text--spacing-none nova-e-text--color-inherit nova-v-publication-item__title"]')
                print(headline[0].text)

            except IndexError as e:
                pass

        pages = content.find_elements_by_class_name('nova-c-button-group__item')
        button = pages[-1]
        button.click()
        page_counter += 1
        
    finally:
        pass
        
driver.quit()