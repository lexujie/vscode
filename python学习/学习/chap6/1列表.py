# 变量可以存储一个元素，而列表可以存储N个元素
from operator import index


lst=['hello','world',98]
print(id(lst))
print(type(lst))
print(lst)

'''列表的创建
   1、使用中括号；
   2、调用内置函数list()'''

lst2=list(['hello','world',98])
print(lst2[0],lst2[-3]) # 索引映射唯一个数据

'''列表的查询操作'''
# 获取列表中指定元素的索引 index()
# 存在相同元素，只返回相同元素中的第一个元素的索引
lst3=['hello','world',98,'hello']
print(lst3.index('hello'))

# 指定范围查找
print(lst3.index('hello',1,4))

# 获取列表中单个元素
# 正向0 - N-1
# 逆向-N - -1
print(lst3[3],lst3[-1])

# 获取列表中的多个元素
# 列表名[start: stop: step],默认步长为1
lst4 = [10,20,30,40,50,60,70,80]
print(lst4[1:6:2])
print(lst4[1:6:])
print(lst4[:6:])
print(lst4[3::])

# 步长为负数，切片第一个元素默认是列表的最后一个元素
print(lst4[::-1]) 
print(lst4[7:3:-1])

# 判断
print(10 in lst4)
print(100 not in lst4)

# 遍历
for i in lst4:
    print(i,end='\t')
