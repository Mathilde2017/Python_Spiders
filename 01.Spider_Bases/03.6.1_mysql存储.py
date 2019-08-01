'''
Python操作Mysql数据库
'''

import pymysql

# 1、连接数据库
db = pymysql.connect(host='localhost',user='root', password='123456', port=3306)
cursor = db.cursor()

cursor.execute('SELECT VERSION()')
data = cursor.fetchone()
print('Database version:', data)

# 2、创建数据库
# 也可以用Navicat等工具操作
# cursor.execute("CREATE DATABASE demo DEFAULT CHARACTER SET utf8")

# 3、创建表
# db = pymysql.connect(host='localhost', user='root', password='123456', port=3306, db='demo')
# cursor = db.cursor()
# sql = """CREATE TABLE IF NOT EXISTS students (
# id VARCHAR(255) NOT NULL,
# name VARCHAR(255) NOT NULL,
# age INT NOT NULL,
# PRIMARY KEY (id))
# """
# cursor.execute(sql)

# 4、插入数据
db = pymysql.connect(host='localhost', user='root', password='123456', port=3306, db='demo')
cursor = db.cursor()
# id = '10'
# name = 'zhang'
# age = 18
#
# sql = 'INSERT INTO students(id, name, age) values(%s, %s, %s)'
# try:
#     cursor.execute(sql, (id, name, age))
#     # 提交执行
#     db.commit()
# except:
#     db.rollback()
# db.close()
    # 事务机制，一旦出错会回滚，不存在一半插入一半没插入的情况。

# 5、更新数据
# sql = 'UPDATE students SET age = %s WHERE name = %s'
#
# try:
#    cursor.execute(sql, (30, 'zhang'))
#    db.commit()
# except:
#    db.rollback()
# db.close()

# 6、删除数据
# table = 'demo'
# condition = 'age < 20'
#
# sql = 'DELETE FROM  {table} WHERE {condition}'.format(table=table, condition=condition)
# try:
#     cursor.execute(sql)
#     db.commit()
#     print("删除成功！")
#     print('Count:', cursor.rowcount)
# except:
#     db.rollback()
# db.close()

# 7、数据查询
sql = 'SELECT * FROM students WHERE age >= 20'
try:
    cursor.execute(sql)
    print('Count:', cursor.rowcount)
    row = cursor.fetchone()
    while row:
        print('Row:', row)
        row = cursor.fetchone()
except:
    print('Error')
db.close()
"""
fetchall()：接受全部返回的结果
fetchone()：获取下一个查询的结果集
rowcount()：只读属性，返回执行语句影响的行数
"""
