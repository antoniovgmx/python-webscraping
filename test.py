# from bs4 import BeautifulSoup
# import requests

# search_param = input()
# url = 'https://www.researchgate.net/search.Search.html?type=publication&query="{}"'.format(search_param)
# print(url)
# response = requests.get(url)
# data = response.text
# soup = BeautifulSoup(data, 'html.parser')

# pages = soup.find_all('span', class_="nova-c-button__label")
# for page in pages:
#     last_page = page.text
#     print(last_page)

# tags = soup.find_all('a', class_="nova-e-link nova-e-link--color-inherit nova-e-link--theme-bare")
# for tag in tags:
#     print(tag.text)

from bs4 import BeautifulSoup
import requests



search_param = input()
url = 'https://www.researchgate.net/search.Search.html?type=publication&query="{}"'.format(search_param)
print(url)
response = requests.get(url)

data = response.text

soup = BeautifulSoup(data, 'html.parser')
print(soup)

tags = soup.find_all('a', class_="nova-e-link nova-e-link--color-inherit nova-e-link--theme-bare")

for tag in tags:
    print(tag.text)