from bs4 import BeautifulSoup
import requests

username = input("Username: ")
url = f'https://github.com/{username}'

request = requests.get(url)

soup = BeautifulSoup(request.text, 'html.parser')

projects = soup.find('ol', class_='d-flex flex-wrap list-style-none gutter-condensed mb-4')

arrprojects = projects.find_all('li', class_='mb-3 d-flex flex-content-stretch col-12 col-md-6 col-lg-6')

for val in arrprojects:
    p = val.find('span', class_='repo').text
    print(p)
