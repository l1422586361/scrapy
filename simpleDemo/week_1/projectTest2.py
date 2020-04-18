from bs4 import BeautifulSoup
import requests
import time

'''
source link: 
    https://weheartit.com/inspirations/taylorswift
Aim:
    craw images from 20 pages to download local

demo:

url = 'https://data.whicdn.com/images/338888035/original.jpg?t=1577683048'

pic = requests.get(url)
with open('images/1.jpg', 'wb') as f:
    print(pic.content)
    f.write(pic.content)

'''


def getImageLinks(urls,data=[]):
    for url in urls:
        print(url)
        wb_data = requests.get(url)
        soup = BeautifulSoup(wb_data.text, 'lxml')
        imgs = soup.select('#main-container > div.grid-responsive > div.col.span-content > div > div > div > div > div > a > img')
        for img in imgs:
            data.append(img.get('src'))
    return data

urls = ['https://weheartit.com/inspirations/taylorswift'] + ['https://weheartit.com/inspirations/taylorswift?page={}'.format(i) for i in range(2,21)]

# print(urls)

# imgLinks = getImageLinks(urls)
# with open('data/project2Links','w') as f:
#     for link in imgLinks:
#         f.write(str(link)+'\n')

with open('data/project2Links','r') as f:
    links = f.readlines()
    i = 0
    for link in links:
        i += 1
        print('%s:%s' % (i,link))
        pic = requests.get(link)
        dir = 'images/'+str(i)+'.jpg'
        with open(dir,'wb') as img:
            img.write(pic.content)