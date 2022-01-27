# 整数类型：int
# 十进制（默认）；二进制（0b开头）；八进制（0o开头）；十六进制（0x开头）
n = 90
print(n,type(n))
print('二进制',0b10101111)
print('八进制',0o176)
print('十六进制',0x1EAF)

# 浮点数类型： float
a = 3.14159
print(a,type(a))
f1 = 1.1
f2 = 2.2
f3 = 2.1
print(f1+f2) # 浮点数存储不精确性
print(f1+f3)

from decimal import Decimal
print(Decimal('1.1')+Decimal('2.2'))

# 布尔类型： bool(True,False)
b1 = True
b2 = False
print(b1 , type(b1))
print(b2 , type(b2))
print(b1+2)
print(b2+2) # bool型可以转成整数计算

# 字符串类型： str
# 不可变的字符序列
# 可以使用单引号，双引号，三引号定义，三引号可以分布在连续的多行，其他不行
str1 = '人生苦短'
str2 = "人生苦短"
str3 = '''人生
苦短'''
str4 = """人
生苦短"""
print(str1,type(str1))
print(str2)
print(str3)
print(str4)


#数据类型转换
name = '张三'
age = 20

print(type(name),type(age)) # 两者数据类型不同
# print('我叫'+name+'今年'+age+'岁') # 不同类型数据连接报错，解决办法，类型转换
print('我叫'+name+'今年'+str(age)+'岁')

# str()将其他类型转成str类型

# int()
# 将str转化成int类型，数字串（整数）可以，小数串和其他不行
# 将float转化为int，截取整数部分，舍去小数

# float()
# 将str转化成float类型，字符串只能为数字串或者小数串

