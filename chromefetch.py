from bs4 import BeautifulSoup
import requests

header = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:88.0) Gecko/20100101 Firefox/88.0'}
"""
mainurl = 'https://www.amazon.de/s?k=Ipad'



searchpade = requests.get(mainurl, headers=header)
search = BeautifulSoup(searchpade.content, 'html.parser')
item = search.find(class_='a-link-normal a-text-normal').get_attribute_list('href')[0]
print(item)
"""
item = '/Neues-Apple-iPad-Air-Wi-Fi-64-GB/dp/B08J6SHYHX'

url = f'https://www.amazon.de{item}'

page = requests.get(url, headers=header)
soup = BeautifulSoup(page.content, 'html.parser')

title = soup.find(id='productTitle').getText()
price = soup.find(id='priceblock_ourprice').getText()

conv_price = float(price[:-1].replace(',', '.'))
print(title.strip())
print(conv_price)
