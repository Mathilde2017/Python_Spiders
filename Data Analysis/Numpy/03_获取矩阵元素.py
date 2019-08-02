import numpy as np

a = np.array( [[2,3,4],[5,6,7]] )
print(a)
print('---'*20)
# 索引从 0 开始
# 获取某个元素，并赋值
a[0,0] = 100
print(a[1,2])   # 7

print(a[1,:])   # [5 6 7]
print(a[1,1:2]) # [6]

a[1,:] = [8,9,10]
print(a)
'''
[[ 100  3  4]
 [ 8  9 10]]
'''
