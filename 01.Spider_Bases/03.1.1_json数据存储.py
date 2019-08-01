'''
dump和 dumps是用来把把字典和数组转换为json格式的，dump把转换结果直接写入文件，dumps返回字符串。
load和 loads是把 json格式的数据转换为字典格式，load直接从json文件中读取数据并返回字典对象，loads把字符串形式的 json数据转换成字典格式。

dump的函数原型是 dump(obj, fp) 第一个参数obj是要转换的对象，第二个参数fp是要写入数据的文件对象。
dumps的函数原型是 dumps(obj) 参数是要转换的对象

注意：如果要转换的对象里有中文字符的话，要把 ensure_ascii设置为 False否则中文会被编码为 ascii格式

load的函数原型是 load(fp) 参数 fp是要读取的文件对象
loads的函数原型是 loads(string) 参数 string是要转换成python对象的json字符串，通常用来将网页中的 json数据转换为 python对象

'''
import json

file_name = 'json_file.txt'
# nums = [3, 4, 5, 7, 1, 9]
nums = {"name": "Mike", "age": 12}
with open(file_name, 'w') as file_obj:
    '''写入json文件'''
    json.dump(nums, file_obj)
    print("写入json文件：", nums)

with open(file_name) as file_obj:
    '''读取json文件'''
    numbers = json.load(file_obj)  # 返回列表数据，也支持字典
    print("读取json文件：", numbers)