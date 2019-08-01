import requests,csv,re
from lxml import etree

headers = {
    "User-Agent" : "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"
}
url = "http://www.seputu.com/"

rsp = requests.get(url,headers)
# print(rsp.text)
html = etree.HTML(rsp.text)

rows = []
# div_title
div_mulus = html.xpath('//*[@class="mulu"]')

for div_mulu in div_mulus:
    div_h2 = div_mulu.xpath('.//div[@class="mulu-title"]/center/h2/text()')
    # print(div_h2) # 有空列表，做下判断
    if len(div_h2)>0:
        h2_title = div_h2[0]

        a_s = div_mulu.xpath('./div[@class="box"]/ul/li/a')
        for a in a_s:
            # 章节链接
            href = a.xpath('./@href')[0]
            # 标题
            box_title = a.xpath('./@title')[0]
            # print(box_title) # [2012-5-23 18:50:0] 盗墓笔记8 第五章（一）

            # 处理时间、章节标题
            pattern = re.compile(r'\s*\[(.*)\]\s+(.*)')
            match = pattern.search(box_title)
            # print(match)

            if match != None:
                date = match.group(1)
                real_title = match.group(2)
                # print(data,real_title)
                content = (h2_title,real_title,href,date)
                # print(content)
                rows.append(content)

heads =['Title','Real_title','Href','Date']
with open('daomu.csv','a',newline='') as f:
    f_csv = csv.writer(f)
    f_csv.writerow(heads)
    f_csv.writerows(rows)