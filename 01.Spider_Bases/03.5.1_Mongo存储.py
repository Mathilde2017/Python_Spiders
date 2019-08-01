"""
MongoDB：非关系型数据库
MongoDB 属于更加适合爬虫的数据库
MongoDB 是一个基于分布式文件存储的数据库，由c++编写
主要为 WEB 应用提供可扩展的高性能数据存储解决方案

概念说明：
SQL         MongoDB     说明：
database    database    数据库
table       collection  表/集合
row         document    行/文档
column      field       字段/域
index       index       索引
primary     primary     主键/_id为主键

"""
import pymongo

# 1、连接数据库
# 连接到数据库，以下两种方式均可
client = pymongo.MongoClient(host='localhost', port=27017)
client = pymongo.MongoClient('mongodb://localhost:27017')
# 注意：默认情况下，MongoDB是没有超级管理员账户的，除非已经在 admin中创建了用户并修改了配置文件，
# 否则不用进行任何认证即可访问、修改数据。
# 下面用密码登录，需要配置，请看浏览器 收藏夹 中内容
# myclient = pymongo.MongoClient('mongodb://root:123456@localhost:27017/')

# 指定连接的数据库，以下两种方式均可
db = client.kugou_db
db = client['kugou_db']

# 指定数据库的某个集合，以下两种方式均可
collection = db.songs
collection = db['songs']

# 2、查询数据
# find_one()， 查询一条记录， 以字典的形式直接返回数据结果。
# find()， 查询多条记录， 返回的是Cursor对象，需要遍历才能获取数据
datas = collection.find()
for data in datas:
    print(data['singer'])
    # 获取集合中的字段属性
    print(data.key())


# 3、插入数据
# 3.1 insert_one(), 一次插入一条记录
post = {
    'name':'zhangsan',
    'sex':'male',
    'age':'18',
    'class':['database','python','java','php']
}

result = post.insert_one(post)
print('post id id:',result.inserted_id)

# 3.2 insert_many(), 一次插入多条记录
book = [
    {
    'name': '五年高考',
    'price': 50,
},
    {
    'name': '三年模拟',
    'price': 30,
},
]
resutl = collection.insert_many(book)
print('post id id:',result.inserted_ids)

# 4、更新数据
# update_one()， 只更新匹配到的第一条记录
# update_many()， 更新匹配到的全部记录
condition = {'name':'五年高考'}
price_change = {'price': 100}

# 方式1
result = collection.update_one(condition,price_change)
print(result)

# 方式2
result = collection.update_one(condition, {'$set': price_change})
print(result)

# 以上两种方式都是更新name为五年高考的字段，但是其结果却是不同的
# 方式一：
# 相当于查询到name为五年高考的字段，将其删除，再将待更新的数据添加上去。结果就是只剩下一个price为100的数据。
#
# 方式二：
# 查询到name为五年高考的字段，仅仅是将price更新为了100，其余不动。
#
# 另外可以调用result.matched_count, result.modified_count来查看匹配的条数和影响的条数。

# 5、删除数据
# delete_one()， 删除符合条件的第一条数据
# delete_many()， 删除符合条件的全部数据

# 删除一条
result = collection.delete_one({'name': '五年高考'})
print(result)

# 删除多条
result = collection.delete_many({'price':50})  # 删除价格为50的全部记录
result = collection.delete_many({'price':{'$gt':30}}) # 删除价格大于30的全部记录
# 另外可以调用result.deleted_count查看删除的条数。

# 6、其他常用方法
# 6.1 count()
count = collection.find().count() # 查询表中全部记录的条数
count = collection.find({'price': {'$gt':30}}).count()  # 价格大于30的条数

# 6.2 sort()
results = collection.find().sort('name', pymongo.ASCENDING) # 按照name升序返回结果
results = collection.find().sort('price', pymongo.DECENDING) # 按照price降序返回结果

# 6.3 limit()
results = collection.find().sort('name', pymongo.ASCENDING).limit(2)  # 限制返回两条结果