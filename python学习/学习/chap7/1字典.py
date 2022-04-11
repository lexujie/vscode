'''字典：python内置的数据结构之一，与列表一样是一个可变序列
         以键值对的方式存储数据，字典是一个无序的序列
         根据key查找value所在位置
         key不能重复，value可以充分
         key是不可变对象'''
# 字典的创建方式
# 1、使用{}创建
scores={'张三':100,'李四':98,'王五':45}
print(scores)
print(type(scores))

# 2、使用dict()
student=dict(name='jack',age=20)
print(student)

# 字典中元素的获取
# 1、使用[]
print(scores['张三'])
#print(scores['陈六']) # KeyError

# 2、使用get()
print(scores.get('张三'))
print(scores.get('陈六'))
print(scores.get('麻七',99)) # 99是在查找'麻七'所对的value不存在时，提供的一个默认值


# key的判断
print('张三' in scores)
print('张三' not in scores)

# 字典元素的删除
del scores['张三']
print(scores)

# 字典元素全部清除
scores.clear()
print(scores)

# 字典元素的新增
scores['陈六']=98
print(scores)

# keys()获取字典所有key
scores={'张三':100,'李四':98,'王五':45}
keys=scores.keys()
print(keys,type(keys))
print(list(keys)) # 将所有key转化为列表

# values()获取字典中所有value
values=scores.values()
print(values,type(values))

# items()获取字典中所有key,value对
items=scores.items()
print(items,type(items))

# 遍历
for i in scores:
    print(i,scores[i],scores.get(i))

'''字典生成式'''
items=['Fruits','Books','Others']
prices=[96,78,85,110,212]
d={item.upper():price for item,price in zip(items,prices)}
print(d)

lst=zip(items,prices)
print(list(lst))
