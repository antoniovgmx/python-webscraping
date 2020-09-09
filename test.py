from bs4 import BeautifulSoup
import requests



search_param = input()
url = 'https://www.researchgate.net/search.Search.html?type=publication&query="{}"'.format(search_param)
print(url)
response = requests.get(url)

data = response.text

soup = BeautifulSoup(data, 'html.parser')

tags = soup.find_all('a', class_="nova-e-link nova-e-link--color-inherit nova-e-link--theme-bare")

for tag in tags:
    print(tag.text)

