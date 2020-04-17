from bs4 import BeautifulSoup
import requests
import time


'''
Source Link:
    http://bj.xiaozhu.com
Aim:
    craw 300 Rental information detail
Detail Include:
    title,address,rent,first images link,landlord or landlady detail(images link,sex,name)
Number:
    300+
'''



urls = ['http://bj.xiaozhu.com'] + ['http://bj.xiaozhu.com/search-duanzufang-p{}-0/'.format(i) for i in range(2,20)]
# print(urls)

def getLink(url,data=None):
    wb_data = requests.get(url)
    # time.sleep(2)
    soup = BeautifulSoup(wb_data.text,'lxml')
    links = soup.select('#page_list > ul > li > a')
    i = 0
    for link in links:
        i += 1
        data = {'index':i ,
                'link':link.get('href'),
                }
        print(data)

def getLinkDatas(urls,max,data=[]):
    for url in urls:
        print(url)
        wb_data = requests.get(url)
        # time.sleep(2)
        soup = BeautifulSoup(wb_data.text, 'lxml')
        links = soup.select('#page_list > ul > li > a')
        for l in links:
            if len(data) >= max:
                print(len(data))
                return data     # return is jump out from this function
            link = l.get('href')
            data.append(link)




for url in urls:
    print(url)
    getLink(url)


links = getLinkDatas(urls,300)
print(links)
print(len(links))


