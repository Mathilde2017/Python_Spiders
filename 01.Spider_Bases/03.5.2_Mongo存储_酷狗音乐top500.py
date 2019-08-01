'''
url = https://www.kugou.com/yy/rank/home/1-8888.html?from=rank
以下为大胆猜想：
https://www.kugou.com/yy/rank/home/1-8888.html?from=rank
https://www.kugou.com/yy/rank/home/2-8888.html?from=rank
......
https://www.kugou.com/yy/rank/home/22-8888.html?from=rank

切换页面信息：
1-23    500
500/22 = 22.7272 故需要1-23页
'''
import requests,pymongo,time
from bs4 import BeautifulSoup

client = pymongo.MongoClient(host='localhost', port=27017)
songes = client.kugou.songs
# print(songs)

headers = {
    "User-Agent" : "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"
}

# 1、获取数据
def kugou(url):
    res = requests.get(url,headers=headers)
    soup = BeautifulSoup(res.text,'lxml')

    ranks = soup.select('.pc_temp_num')
    titles = soup.select('.pc_temp_songlist > ul > li > a')
    times = soup.select('.pc_temp_time')

    for rank,title,time in zip(ranks,titles,times):
        # 页面下方延伸 zip() 的用法
        rank = rank.get_text().strip()
        song = title.get_text().split('-')[-1].strip()
        singer = title.get_text().split('-')[0].strip()
        song_time = time.get_text().strip()
        # print(rank, song, singer, song_time)

        # 封装数据
        data = {
            'rank':rank,
            'song':song,
            'singer':singer,
            'song_time':song_time
        }

        return data
        # print(type(data))
        # print(data)

# 2、保存到MongoDB
def save_mongo(data):
    songs_id = songes.insert_many(data).inserted_ids
    print(songs_id)


if __name__ =='__main__':
    # urls = "https://www.kugou.com/yy/rank/home/1-8888.html?from=rank"
    urls = ["https://www.kugou.com/yy/rank/home/{}-8888.html?from=rank".format(str(i)) for i in range(1,24)]
    # print(urls)
    for url in urls:
        data = kugou(url)
        save_mongo(data)
        # time.sleep(1)

# 延伸 zip()
# zip() 函数用于将可迭代的对象作为参数，将对象中对应的元素打包成一个个元组，然后返回由这些元组组成的列表。
# 如果各个迭代器的元素个数不一致，则返回列表长度与最短的对象相同，利用 * 号操作符，可以将元组解压为列表。
# zip([iterable, ...])
# a = [1,2,3]
# b = [4,5,6]
# c = [4,5,6,7,8]
#
# zipped1 = zip(a,b) # 打包为元组的列表
# for zi in zipped1:
#     print(zi)
# # (1, 4) (2, 5) (3, 6)
#
# zipped2 = zip(a,c) # 元素个数与最短的列表一致
# for i in zipped2:
#     print(i)
# # (1, 4), (2, 5), (3, 6)
#
# ziii = zip(*zipped1)          # 与 zip 相反，*zipped 可理解为解压，返回二维矩阵式
# for zi in ziii:
#     print(zi)
