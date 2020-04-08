from bs4 import BeautifulSoup
import requests



headers = {
    'User-Agent' : ''
}

url = ''

mb_data = requests.get(url,headers=headers)
soup = BeautifulSoup(mb_data.text,'lxml')
imgs = soup.select('')
for i in imgs:
    print(i.get('src'))