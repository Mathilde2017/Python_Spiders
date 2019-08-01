from XcSpider.items import XiciDailiItem
from XcSpider.mysqlpipeline.sql import Sql

class XiciDailiPipeline():
    def process_item(self,item,spider):
        if isinstance(item,XiciDailiItem):
            ipaddress = item['ipaddress']
            ret = Sql.select_name(ipaddress)

            if ret[0] ==1:
                print("已经存在啦~~~~")
            else:
                country = item['country']
                ipaddress = item['ipaddress']
                port = item['port']
                serveraddr = item['serveraddr']
                isanonymous = item['isanonymous']
                type = item['type']
                alivetime = item['alivetime']
                verifictiontime = item['verifictiontime']

                Sql.insert_db_xici(country,ipaddress,port,serveraddr,isanonymous,type,alivetime,verifictiontime)


# 去 setting 中开启 ITEM_PIPELINES