'''
中国票房网数据：
url = http://www.cbooo.cn/
'''

import pandas as pd
import requests
from bs4 import BeautifulSoup

url = 'http://www.cbooo.cn/year?year=2018'
datas = requests.get(url).text
# print(datas)

soup = BeautifulSoup(datas,'lxml')
movies_table = soup.find_all('table',{'id':'tbContent'})[0]
# print(movies_table)

movies = movies_table.find_all('tr')

# 获取电影名称
names = [tr.find_all('td')[0].a.get('title') for tr in movies[1:]]
# print(names)

# 获取电影url地址
hrefs = [tr.find_all('td')[0].a.get('href') for tr in movies[1:]]
# print(hrefs)

# 电影类型
types = [tr.find_all('td')[1].string for tr in movies[1:]]
# print(types)

# 总票房数据
boxoffice = [int(tr.find_all('td')[2].string) for tr in movies[1:]]
# print(boxoffice)

# 平均票价
mean_price = [int(tr.find_all('td')[3].string) for tr in movies[1:]]
# print(mean_price)

# 场均人次
mean_people = [int(tr.find_all('td')[4].string) for tr in movies[1:]]
# 国家和地区
countries = [tr.find_all('td')[5].string for tr in movies[1:]]

# 获取上映时间
times = [tr.find_all('td')[6].string for tr in movies[1:]]

# 导演
def getInfo(url):
    datas = requests.get(url)
    soup = BeautifulSoup(datas.text,'lxml')

    daoyan = soup.select('dl.dltext dd')[0].get_text()
    return daoyan

directors = [getInfo(url).strip('\n') for url in hrefs]
# print(directors)

df = pd.DataFrame({
    'name':names,
    'href':hrefs,
    'type':types,
    'boxoffice':boxoffice,
    'mean_price':mean_price,
    'mean_people(万)':mean_people,
    'countries':countries,
    'time':times,
    'director':directors
})
# print(df)
# print(df.head())

df.to_csv('movie.csv')