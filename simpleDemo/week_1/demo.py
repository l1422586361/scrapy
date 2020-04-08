from bs4 import BeautifulSoup
import requests
import time



url = 'http://www.nnaa44.link/cexz5/22.html'
urls = ['http://www.nnaa44.link/cexz5/22.html'] + ['http://www.nnaa44.link/cexz5/22/{}.html'.format(str(i)) for i in range(2,101)]
# urls.insert(0,'http://www.nnaa44.link/cexz5/22.html')
# print(urls)



def get_attractions(url,data=None):
    wb_data = requests.get(url)
    time.sleep(3)
    soup  = BeautifulSoup(wb_data.text,'lxml')
    # print(soup)
    titles = soup.select('div.mainArea.px17 > ul > li > a > h3')
    imgs = soup.select('div.mainArea.px17 > ul > li > a > img')
    links = soup.select('div.mainArea.px17 > ul > li > a')
    for title,img,link in zip(titles,imgs,links):
        data = {
            'title' : title.get_text(),
            'img' : 'http://www.nnaa44.link' + img.get('src'),
            'link' : 'http://www.nnaa44.link' + link.get('href'),
        }
        if data['title']:
            print(data)



# get_attractions(url)


for single_url in urls:
    get_attractions(single_url)

