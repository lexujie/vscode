# 元组：python内置的数据结构之一，是一个不可变序列（没有增，删，改操作）
'''可变序列：列表，字典，集合'''
'''不可变序列：字符串，元组'''

'''元组的创建方式'''
# 1、使用()
t=('Python','world',98)
print(t,type(t))

t2='Python','world',98
print(t2,type(t2))

t3=('apple')
print(t3,type(t3)) # 只包含一个元素要使用逗号

t4=('apple',)
print(t4,type(t4))

t5=()
t6=tuple() # 空元组的创建
# 2、使用内置函数tuple()
t1=tuple(('Python','world',98))
print(t1,type(t1))

# 元组不可变性，列表的可变性
y=(10,[20,30],9)
print(y,type(y))
print(y[0],type(y[0]),id(y[0]))
print(y[1],type(y[1]),id(y[1]))
print(y[2],type(y[2]),id(y[2]))

# t[1]=100 TypeError: 'tuple' object does not support item assignment
y[1].append(100)
print(y)

# 遍历
for i in t:
    print(i)