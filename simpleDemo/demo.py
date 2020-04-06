from bs4 import BeautifulSoup
import requests

url = 'https://www.bilibili.com/ranking?spm_id_from=333.851.b_7072696d61727950616765546162.3'
wb_data = requests.get(url)
soup = BeautifulSoup(wb_data.text,'lxml')
titles = soup.select('div.info > a.title')
imgs = soup.select('div.lazy-img.cover > img')
cates = soup.select('div.info > div.detail > a > span')

for title,img,cate in zip(titles,imgs,cates):
    data = {
        'title':title.get_text(),
        # 'img':img.get('alt'),
        'img2':img.get('src'),
        'cate':cate.get_text(),
    }
    print(data)
print(111)