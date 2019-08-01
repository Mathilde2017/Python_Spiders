'''
CSV (Comma-Separated Values)，逗号分隔值
其文件以纯文本形式存储表格数据（数字和文本）
有时也称为字符分隔值，因为分隔字符也可以不是逗号

ID,name,age
1001,zhangsan,18
1002,lisi,20
'''

import csv
headers = ['ID','name','age']

rows =[
    (1001,'zhangsan',18),
    (1002,'lisi',20)
]

with open('test.csv','w') as f:
    # csv.writer()方法初始化一个写入对象
    f_csv = csv.writer(f)
    f_csv.writerow(headers)
    f_csv.writerows(rows)
