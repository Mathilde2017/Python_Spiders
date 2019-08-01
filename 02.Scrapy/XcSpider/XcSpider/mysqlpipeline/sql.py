import pymysql
from XcSpider import settings

MYSQL_HOSTS = settings.MYSQL_HOSTS
MYSQL_USER = settings.MYSQL_USER
MYSQL_PASSWORD = settings.MYSQL_PASSWORD
MYSQL_PORT = settings.MYSQL_PORT
MYSQL_DB = settings.MYSQL_DB


db = pymysql.connect(user=MYSQL_USER,password=MYSQL_PASSWORD,host=MYSQL_HOSTS,port=MYSQL_PORT,database=MYSQL_DB,charset="utf8")
cursor = db.cursor()

class Sql():
    @classmethod
    def insert_db_xici(cls,country,ipaddress,port,serveraddr,isanonymous,type,alivetime,verifictiontime):
        sql = "insert into xicidaili(country,ipaddress,port,serveraddr,isanonymous,type,alivetime,verifictiontime) VALUES(%(country)s,%(ipaddress)s,%(port)s,%(serveraddr)s,%(isanonymous)s,%(type)s,%(alivetime)s,%(verifictiontime)s)"
        value = {
            "country":country,
            "ipaddress":ipaddress,
            "port":port,
            "serveraddr":serveraddr,
            "isanonymous":isanonymous,
            "type":type,
            "alivetime":alivetime,
            "verifictiontime":verifictiontime
        }
        
        try:
            cursor.execute(sql,value)
            db.commit()
        except Exception as e:
            print(e)
            print("插入失败！！！")
            db.rollback()
    
    @classmethod
    # 去重
    def select_name(cls,ipaddress):
        sql = "select exists (select 1 from xicidaili where ipaddress=%(ipaddress)s )"
        value = {
            "ipaddress": ipaddress
        }
        
        cursor.execute(sql,value)
        return cursor.fetchall()[0]
            
        
