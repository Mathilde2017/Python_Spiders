# 步骤
## 一、创建爬虫
    - scrapy startproject xcdl
    - cd xcdl
    - scrapy genspider xcdl xicidaili.com

## 二、定义爬行字段
    - items.py 中设置
        - country = scrapy.Field()
        - ipaddress = scrapy.Field()
        - ...
## 三、编写 spider 文件
    - 分析页面结构
    - 提取数据
    - 传送数据到 pipeline

## 四、编写 pipeline文件
### 4.1 编写 mysql
    - 基本配置
    - 外部引用
### 4.2 编写 MongoDB
    - 基本配置
    - 直接写在 pipelines.py 中
  
## 五、编写设置文件 setting.py 
    - 关闭 robots 
    - 设置 请求头 信息：根据网站 network决定 
    - 开启
    
    
    
## 六、在任意 目录下 编写一个 main.py
    - 代码：
        - from scrapy import cmdline
        - cmdline.execute('scrapy crawl xcdl'.split())
        
    - 目的：直接运行该文件，即可 实现 在 cmd 窗口中的 scrapy crawl xcdl 运行爬虫效果

## 七、建 MySQL 数据库
    - create database db_xici
    - use db_xici

    - create table `xicidaili`(
    `id` int(255) unsigned NOT NULL AUTO_INCREMENT,
    `country` varchar(1000) NOT NULL,
    `ipaddress` varchar(1000) NOT NULL,
    `port` int(255) NOT NULL,
    `serveraddr` varchar(50) NOT NULL,
    `isanonymous` varchar(30) NOT NULL,
    `type` varchar(30) NOT NULL,
    `alivetime` varchar(30) NOT NULL,
    `verifictiontime` varchar(30) NOT NULL,
    PRIMARY KEY(`id`)
    )ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;

## MongoDB 操作
    - cmd  cd C:\Program Files\MongoDB\Server\4.0\bin
    - mongo
    - show dbs  查看所有的数据库
    - db    查看当前的数据库名称
    - show collection 查看当前数据库下的集合
    - use   test(数据库的名称) 切换到指定的数据库

    - db.集合名.操作  对集合进行某种操作
    - use xicidaili
    - db.xicidaili.find()

 ## 设置 User-Agent 的方式
 ### 1、setting 和 spiders 配合使用
       - setting中如下：
       - MY_USER_AGENT = [
            "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:21.0) Gecko/20100101 Firefox/21.0",
            "Mozilla/5.0 (Android; Mobile; rv:14.0) Gecko/14.0 Firefox/14.0",
            "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.94 Safari/537.36",
            "Mozilla/5.0 (Linux; Android 4.0.4; Galaxy Nexus Build/IMM76B) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.133 Mobile Safari/535.19"
        ]

        - headers = {
            'User-Agent':random.choice(MY_USER_AGENT),
            'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Accept-Language':'zh-CN,zh;q=0.9',
            'Upgrade-Insecure-Requests':1
        }

        - spiders中的用法
        - from LianjiaSpider.settings import headers
        - def start_requests(self):
            start_urls = [
                'https://cd.lianjia.com/zufang/qingyang/pg1l1rp3/',
                'https://cd.lianjia.com/zufang/pidou/pg1l1rp3/'
            ]
        - for start_url in start_urls:
            yield scrapy.Request(url=start_url,callback=self.parse,dont_filter=True,headers=headers)

 ### 2、setting 和 pipeline中用法