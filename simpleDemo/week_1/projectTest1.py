from bs4 import BeautifulSoup
import requests
import time

url_1 = ['http://bj.xiaozhu.com']
url_2 = ['http://bj.xiaozhu.com/search-duanzufang-p{}-0/'.format(i) for i in range(2,10)]
urls = url_1 + url_2

def getLink(url,data=None):
    wb_data = requests.get(url)
    time.sleep(2)
    soup = BeautifulSoup(wb_data.text,'lxml')
    links = soup.select('#page_list > ul > li > a')
    i = 0
    for link in links:
        i += 1
        data = {'index':i ,
                'link':link.get('href'),
                }
        print(data)

for url in urls:
    print(url)
    getLink(url)


