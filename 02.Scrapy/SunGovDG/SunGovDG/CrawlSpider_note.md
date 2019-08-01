# Crawl Spider 
## 一、简单介绍
    Scrapy框架中分两类爬虫，Spider类和CrawlSpider类。
    CrawlSpider是Spider的派生类，Spider类的设计原则是只爬取start_url列表中的网页；
    而CrawlSpider类定义了一些规则(rule)来提供跟进link的方便的机制，从爬取的网页中获取link并继续爬取。
 
## 二、创建爬虫模板
    scrapy genspider -t crawl spidername www.xxxx.com
    
## 三、方法属性
    3.1 LinkExtractors
    Link Extractors 的目的是提取链接，调用的是extract_links(),其提供了过滤器(filter),以便于提取包括符合正则表达式的链接。 
    过滤器通过以下构造函数的参数配置:
        allow (a regular expression (or list of)) – 必须要匹配这个正则表达式(或正则表达式列表)的URL才会被提取如果没有给出(或为空), 它会匹配所有的链接
        deny (a regular expression (or list of)) – 与这个正则表达式(或正则表达式列表)的(绝对)不匹配的URL必须被排除在外(即不提取)它的优先级高于 allow 的参数如果没有给出(或None), 将不排除任何链接
        allow_domains (str or list) – 单值或者包含字符串域的列表表示会被提取的链接的domains
        deny_domains (str or list) – 单值或包含域名的字符串,将不考虑提取链接的domains
        deny_extensions (list) – 应提取链接时,可以忽略扩展名的列表如果没有给出, 它会默认为 scrapy.linkextractor 模块中定义的 IGNORED_EXTENSIONS 列表
        restrict_xpaths (str or list) – 一个的XPath (或XPath的列表),它定义了链路应该从提取的响应内的区域如果给定的,只有那些XPath的选择的文本将被扫描的链接见下面的例子
        tags (str or list) – 提取链接时要考虑的标记或标记列表默认为 ( 'a' , 'area') 
        attrs (list) – 提取链接时应该寻找的attrbitues列表(仅在 tag 参数中指定的标签)默认为 ('href')
        canonicalize (boolean) – 规范化每次提取的URL(使用scrapy.utils.url.canonicalize_url )默认为 True 
        unique (boolean) – 重复过滤是否应适用于提取的链接
        process_value (callable) – 见:class:BaseSgmlLinkExtractor 类的构造函数 process_value 参数
    3.2 Rules:
    在rules中包含一个或多个Rule对象，每个Rule对爬取网站的动作定义了特定操作。
    如果多个rule匹配了相同的链接，则根据规则在本集合中被定义的顺序，第一个会被使用。
        callback： 从link_extractor中每获取到链接时，参数所指定的值作为回调函数，该回调函数接受一个response作为其第一个参数。 注意：当编写爬虫规则时，避免使用parse作为回调函数。由于CrawlSpider使用parse方法来实现其逻辑，如果覆盖了 parse方法，crawl spider将会运行失败。
        follow：是一个布尔(boolean)值，指定了根据该规则从response提取的链接是否需要跟进。 如果callback为None，follow 默认设置为True ，否则默认为False。
        process_links：指定该spider中哪个的函数将会被调用，从link_extractor中获取到链接列表时将会调用该函数。该方法主要用来过滤。
        process_request：指定该spider中哪个的函数将会被调用， 该规则提取到每个request时都会调用该函数。 (用来过滤request)
    