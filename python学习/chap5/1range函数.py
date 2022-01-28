# range()函数：用于生成一个整数序列，不管序列多长，占用的内存相同

r = range(10) # 默认从0开始，默认相差1（步长）
print(r)
print(list(r)) # list用于查看range对象中的整数序列

r2 = range(1,10) # 指定起始
print(list(r2))

r3 = range(1,10,2) # 指定起始和步长
print(list(r3))

# in和not in 判断整数序列中是否存在指定的整数
print(10 in r)
print(10 not in r2) 