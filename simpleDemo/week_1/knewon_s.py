from bs4 import BeautifulSoup
import requests
import time


url = 'https://knewone.com/discover?page='

def get_page(url,data=None):
    wb_data = requests.get(url,headers=headers)
    soup  = BeautifulSoup(wb_data.text,'lxml')
    titles = soup.select('div.property_title > a[target="_blank"]')
    imgs = soup.select('img[width="160"]')
    cates = soup.select('div.p13n_reasoning_v2')
    for title,img,cate in zip(titles,imgs,cates):
        data = {
            'title' : title.get_text(),
            'img' : img.get('src'),
            'cate' : list(cate.stripped_strings),
        }
        print(data)


def get_more_pages(start,end):
    for one in range(start,end):
        get_page(url+str(one))
        time.sleep(2)

get_more_pages(1,10)