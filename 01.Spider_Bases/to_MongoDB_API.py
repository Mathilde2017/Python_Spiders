from pymongo import MongoClient

client = MongoClient('127.0.0.1', 27017)   # 本地IP，默认端口
print(client)
# db = client['test']  # 进入数据库
# col = db['test_set']   # 进入集合

# class MongoAPI(object):
#     def __init__(self,db_ip,db_port,db_name,table_name):
#         self.db_ip = db_ip
#         self.db_port = db_port
#         self.db_name = db_name
#         self.table_name = table_name
#
#         self.conn = MongoClient(host=self.db_ip,port=self.db_port)
#
#         self.db = self.conn[self.db_name]
#         self.table = self.db[self.table_name]
#
#
#     def get_one(self,query):
#         return self.table.find_one(query,property={"_id":False})
#
#     def get_all(self,query):
#         return self.table.find(query)
#
#     def add(self,kv_dict):
#         return self.table.insert(kv_dict)
#
#     def delete(self,query):
#         return self.table.delete_many(query)
#
#     # 查看集合中是否包含满足条件的数据，如有则返回true，没有就新建
#     def check(self,query):
#         ret = self.table.find_one(query)
#         return ret !=None
#
#     def update(self,query,kv_dict):
#         self.table.update_one(query,{'$set':kv_dict},upsert=True)