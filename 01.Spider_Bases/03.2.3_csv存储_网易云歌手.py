'''
网易云音乐歌手信息提取
原地址：https://music.163.com/#/discover/artist/cat?id=2001&initial=66   凡是有 # ，一般都不是真实地址。
打开 f12 ，发现真实地址：
url = https://music.163.com/discover/artist/cat?id=1001&initial=66

id = 1001 歌手类别  1001,1002,1003,2001,2002,2003,6001....
initial = 66  分析发现规律：[-1,65-90,0]
'''

import requests,csv
from bs4 import BeautifulSoup

def get_artists(url):
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
        'Referer':'https://music.163.com/',
        'Host':'music.163.com'
    }
    rsp = requests.get(url,headers=headers)
    soup = BeautifulSoup(rsp.text,'lxml')

    for item in soup.find_all('a',attrs={'class':'nm nm-icn f-thide s-fc0'}):
        artist_name = item.string.strip()
        artist_id = item['href'].replace('/artist?id=','').strip()
        # artist_name = item.string
        # artist_id = item['href']
        # print(artist_id,artist_name)
        try:
            writer.writerow((artist_id,artist_name))
        except Exception as e:
            print("写入失败！！！")
            print(e)

if __name__ == '__main__':
    id_list = [1001,1002,1003,2001,2002,2003,6001,6002,6003,7001,7002,7003,4001,4002,4003]
    init_list = [-1,0,65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90]
    # a = [x for x in range(65,91)]
    # print(a)

    # 文件存储位置：
    csvfile = open('music_163_artist.csv','a',encoding='utf-8')
    writer = csv.writer(csvfile)
    writer.writerow(('artist_id','artist_name'))

    for i in id_list:
        for j in init_list:
            url = "https://music.163.com/discover/artist/cat?id={}&initial={}".format(i,j)
            # print(url)
            get_artists(url)


