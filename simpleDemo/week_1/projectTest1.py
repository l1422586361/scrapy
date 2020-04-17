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



#
# for url in urls:
#     print(url)
#     getLink(url)


# links = getLinkDatas(urls,300)
# print(links)
# print(len(links))

# input links to projectLinks
# with open('data/projectLinks','w') as f:
#     for link in links:
#         f.write(link+'\n')


def getDetailFromLinks(url,data=None):
    wb_data = requests.get(url)
    # time.sleep(1)
    soup = BeautifulSoup(wb_data.text,'lxml')
    # print(soup)
    titles = soup.select(' div.con_l > div.pho_info > h4 > em')
    addresses = soup.select(' div.con_l > div.pho_info > p > span')
    rents = soup.select('#pricePart > div.day_l > span')
    houseImages = soup.select('#curBigImage')
    manImages = soup.select('#floatRightBox > div.js_box.clearfix > div.member_pic > a > img')
    manName = soup.select('#floatRightBox > div.js_box.clearfix > div.w_240 > h6 > a')
    manSex = soup.select('#floatRightBox > div.js_box.clearfix > div.w_240 > h6 > span')
    # print(titles,addresses,rents,houseImages,manImages,manName,manSex)
    for title,address,rent,houseImage,manImage,name,sex in zip(titles,addresses,rents,houseImages,manImages,manName,manSex):
        data = {
            'title': title.get_text(),
            'address': address.get_text(),
            'rent': '$'+ rent.get_text(),
            'houseImage': houseImage.get('src'),
            'manImage': manImage.get('src'),
            'manName': name.get('title'),
            'manSex': 'boy' if str(sex.get('class')).find('boy') > 0 else 'girl',
        }
        # print(data)
        return data

#   input detail tu projectLinks file
#
# with open('data/projectLinks','r') as f:
#     links = f.readlines()
#     i = 0
#     for link in links:
#         i += 1
#         detail = getDetailFromLinks(link)
#         detail['link'] = str(link).replace('\n','')
#         with open('data/projectDatas','a+') as d:
#             print(i)
#             d.write(str(detail).replace('\n','')+'\n')

#
# with open('data/projectDatas','r') as f:
#     details = f.readlines()
#     for detail in details:
#         # print(eval(detail)['link'])
#         with open('data/projectLinks','a+') as d:
#             d.write(eval(detail)['link']+'\n')

