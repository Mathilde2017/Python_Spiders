from selenium import webdriver
from scrapy.http import HtmlResponse
import time

class XiaoHuaDownloaderMiddlewares(object):
    def process_request(self, request, spider):
        print('开始打印 request spider对象')
        print(request,type(request))
        print(spider,type(spider))

        print('打印完成')
        '''
        自定义爬虫下载中间件
        :param request: 请求对象
        :param spider: 请求爬虫
        :return:
        '''
        driver = webdriver.Chrome()
        driver.get(request.url)
        time.sleep(2)
        driver.save_screenshot('1.png')

        js = 'document.body.scrollTop=10000'
        driver.execute_script(js)

        time.sleep(4)
        driver.save_screenshot('2.png')

        html = driver.page_source
        driver.quit()

        # 一定记着 return
        # HtmlResponse 对应的是爬虫中的 parse 函数

        # 我们要对接Selenium进行抓取，在这里采用Downloader Middleware来实现，在Middleware里面的process_request()
        # 方法里面对每个抓取请求进行处理，启动浏览器并进行页面渲染，再将渲染后的结果构造一个HtmlResponse返回即可。

        # 当process_request() 方法返回Response对象的时候，接下来更低优先级的Downloader Middleware的process_request()
        # 和process_exception() 方法就不会被继续调用了，转而依次开始执行每个Downloader Middleware的process_response()
        # 方法，调用完毕之后直接将Response对象发送给Spider来处理。

        # 在这里我们直接返回了一个HtmlResponse对象，它是Response的子类，同样满足此条件，返回之后便会顺次调用每个Downloader
        # Middleware的process_response()方法，而在process_response() 中我们没有对其做特殊处理，接着他就会被发送给Spider，
        # 传给Request的回调
        print('自定义中间件下载完成')
        return HtmlResponse(url=request.url,encoding='utf-8',body=html,request=request)
