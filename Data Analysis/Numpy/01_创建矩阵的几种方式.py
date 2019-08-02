import numpy as np

# 一、np.arange()方式
t1 = np.arange(12)
# 一维数组被打印成行，二维数组成矩阵，三维数组成矩阵列表。
print(t1,type(t1))
# 矩阵支持四则运算（矩阵每个元素分别进行运算）
t1 = t1 + 2
print(t1,type(t1),t1.shape)
print(t1.reshape(3,4))
print('---'*20)
print(t1.reshape(2,2,3))
print('---'*20)
'''
    ndarray.shape 数组的维度。这是一个指示数组在每个维度上大小的整数元组。
    ndarray.reshape 改变矩阵的形状，可以实现 一维、二维、三维等高维的相互转换
    ndarray.dtype 一个用来描述数组中元素类型的对象，可以通过创造或指定dtype使用标准Python类型
'''

li = [1,2,3,4,5]
# li = li + 2
# print(li,type(li))    # 直接报错

# 二、ndarray.array() 方式
# 以list或tuple变量为参数产生一维数组
# 这种运用最多,方便从数据库提取、存储数据
t2 = np.array(([1,2,3,4],
              [5,6,7,8],
              [9,10,11,12]))
print(t2)

data = ([1,2,3],[True,5,False])
t2a = np.array(data)
print(t2a)

# 生成数组的时候，可以指定数据类型，例如numpy.int32, numpy.int16, and numpy.float64
t2b = np.array((1.2,2,3,4), dtype=np.int32)
print(t2b)

print('---第三种方式---')
# 三、ndarray.random.random()
# 生成随机浮点数，取值范围：[0,1)
t3 = np.random.random(6)
print(t3)
print('---'*20)
t3a = np.random.random(size=[3,2,2])
print(t3a)

# np.random.randint()、np.random.ranom.random_integers()：
# 生成均匀分布的整数。根据所传的参数，前者范围为[start,end)，后者为[start,end]
t3b = np.random.randint(1,100,size=(2,2))
print(t3b)
# np.random.randn()：随机生成服从正态分布~N(0,1)的浮点数
# np.random.rand()：随机生成均匀分布的[0,1]的随机小数

print('---第四种---')
# 四、函数创建
# 使用numpy.zeros，numpy.ones，numpy.eye等方法可以构造特定的矩阵
'''
    函数 zeros 创建一个全是0的数组，
    函数 ones 创建一个全1的数组，
    函数 empty 创建一个内容随机并且依赖与内存状态的数组。
    默认创建的数组类型(dtype)都是float64。
'''
print(np.zeros((2,3)))
print(np.ones((2,2)))
print(np.empty((3,4)))

