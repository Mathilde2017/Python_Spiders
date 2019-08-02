import numpy as np

# 常见属性
'''
ndarray.ndim
数组轴的个数，在python的世界中，轴的个数被称作秩

ndarray.shape
数组的维度。这是一个指示数组在每个维度上大小的整数元组。例如一个n排m列的矩阵，它的shape属性将是(2,3),
这个元组的长度显然是秩，即维度或者ndim属性

ndarray.size
数组元素的总个数，等于shape属性中元组元素的乘积。

ndarray.dtype
一个用来描述数组中元素类型的对象，可以通过创造或指定dtype使用标准Python类型。另外NumPy提供它自己的数据类型。

ndarray.itemsize
数组中每个元素的字节大小。例如，一个元素类型为float64的数组itemsiz属性值为8(=64/8),
又如，一个元素类型为complex32的数组item属性为4(=32/8).

ndarray.data
包含实际数组元素的缓冲区，通常我们不需要使用这个属性，因为我们总是通过索引来使用数组中的元素。
'''
print('---常见属性---')
t1 = np.arange(12).reshape(3,4)
print(t1,type(t1),t1.shape)

print('矩阵元素的数量：',t1.size)   # 12  ，即：3*4 = 12
print('元素类型：',t1.dtype) # int32
print('每个元素所占的字节数：',t1.itemsize) # 4

t1b = t1.astype(np.float64)
print('每个元素所占的字节数：',t1b.itemsize) # 8

# 二、降维
print('--------------矩阵升降维--------------')
# (100,10,10) => (1000,10)
t2 = np.arange(12).reshape(3,4)
# 矩阵运算：就是对 矩阵中的每个元素分别进行运算。
t2a = t2 + 4
print(t2a)
'''
降维操作
ndarray.flatten(order='C') 返回一个折叠成一维的数组。但是该函数只能适用于numpy对象
关于 order ，默认 为 'C'；
C	折叠成行为主（C型）顺序的方法
F	折叠成列为主（Fortran-型）顺序的方法
A	如果a在内存中是Fortran，以列为主排序平坦的方式，否则以列为主排序。
K	按元素在存储器中顺序排列的方
'''
t2b = t2.flatten(order='C')
print(t2b)

# 三、四则运算
print('----------四则运算 +、-、* / ----------')
t3 = np.arange(6).reshape(2,3)
print(t3)
t4 = np.array(([1,3,9],[2,4,8]))
print(t4)

t3a = t3 * t4
print(t3a)

# 矩阵的尺寸可以不同，但是必须 (?,1) (1,?)
print('----------矩阵的尺寸可以不同，但是必须 (?,1) (1,?)----------')
t5 = np.arange(12).reshape(1,12)
t6 = np.arange(12).reshape(12,1)

t5a = t5 + t6
print(t5a)
