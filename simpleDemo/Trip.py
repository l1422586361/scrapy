from bs4 import BeautifulSoup
import request
import time


url_saves = ''
url = ''
urls = ['{}'.format(str(i)) for i in range(30,930,30)]

headers = {
    'User-Agent':'',
    'Cookie':''
}

def get_attractions(url,data=None):
    wb_data = request.get(url)
    time.sleep(2)
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


def get_favs(url,data=None):
    wb_data = request.get(url,headers=headers)
    time.sleep(2)
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

for single_url in urls:
    get_attractions(single_url)