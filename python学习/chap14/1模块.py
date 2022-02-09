'''
模块
一个模块可以包含N个函数
一个扩展名为.py的文件就是一个模块
'''

'''
创建模块
创建一个.py文件

导入模块
import 模块名称 [as 别名]

from 模块名称 import 函数/变量/类
'''
# 关于数学计算的模块
import math
print(id(math),type(math),math)
print(math.pi)
print('------------------')
print(dir(math))
print(math.pow(2,3))

from math import log10
print(log10(1000))

# 导入自定义模块,需要在终端打开chap14
import calc
print(calc.add(10,90))
print(calc.div(10,2))