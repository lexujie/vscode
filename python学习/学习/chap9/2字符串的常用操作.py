'''查询'''
#index()查找子串第一次出现的位置，不存在，则错误
from cmath import pi
from posixpath import split


s='hello,hello'
print(s.index('lo'))
#rindex()查找子串最后一次出现的位置，不存在，则错误
print(s.rindex('lo'))
#find()查找子串第一次出现的位置，不存在，则返回-1
print(s.find('lo'))
print(s.find('s'))
#rfind()查找子串最后一次出现的位置，不存在，则返回-1
print(s.rfind('lo'))

'''大小写转化:会产生新的字符串'''
# upper()将所有字符传化为大写
w='leXuJie,MaJiaqi'
print(w.upper())
# lower()将所有字符转化为小写
print(w.lower())
# swapcase()将所有大写转化为小写，所有小写转化为大写
print(w.swapcase())
# capitalize()把第一个字符转换为大写，其余的转化为小写
print(w.capitalize())
# title()把每个单词第一个字母转换为大写，剩余为小写
print(w.title())

'''内容对齐'''
# center()居中对齐，第一个参数为宽度，第二个为填充符，默认为空格，设置宽度小于实际宽度则返回原字符
x='hello,Python'
print(x.center(20,'*'))
# ljust()左对齐，第一个参数为宽度，第二个为填充符，默认为空格，设置宽度小于实际宽度则返回原字符
print(x.ljust(20,'*'))
print(x.ljust(10,'*'))
# rjust()右对齐，第一个参数为宽度，第二个为填充符，默认为空格，设置宽度小于实际宽度则返回原字符
print(x.rjust(20))
# zfill()右对齐，左边用0填充，只有一个参数为宽度，设置宽度小于实际宽度则返回原字符
print(x.zfill(20))
print('-8910'.zfill(10))

'''劈分'''
# split()从左开始，默认劈分空格，返回一个列表
# 通过参数sep指定劈分字符串
# 通过参数maxsplot指定最大劈分次数
p='hello world python'
print(p.split())
print(p.split(sep='o',maxsplit=1))

# rsplit()从右开始，其他相同
print(p.rsplit(sep='o',maxsplit=1))

'''判断'''
# isidentifier()判断指定的字符串是不是合法的标识符
d='hello,python'
print(d.isidentifier())
d1='hello_python'
print(d1.isidentifier())
# isspace()判断字符串是否全由空白字符组成（回车，换行，水平制表）
print('\t'.isspace())
# isalpha()判断字符串是否全为字母
print('张三'.isalpha())
# isdecimal()判断字符串是否全为十进制数字
print('2321'.isdecimal())
# isnumeric()判断字符串是否全为数字
print('三'.isnumeric())
# isalnum()判断字符串是否全为字母和数字
print('as12张'.isalnum())


'''替换合并'''
# replace()替换，第一个参数为被替换的子串，第二个为替换的子串，第三个为最大替换次数（可省略）
r='hello'
print(r.replace('l','v',1))
# join()将列表或元组中的字符串合并成一个字符串
lst=['le','xu','jie']
print(''.join(lst))
print('*'.join('Python'))

'''比较
   规则：先比较两个字符串第一个字符，相等则进行下一个，直到不相等，后续不再比较
   原理：比较的是ordinal value'''

print('apple'>'app')
print('apple'>'banana')
print(ord('a'),ord('b')) # ASCII码
print(chr(97),chr(98))

# ==比较的是value，is比较的是id

'''切片[start:end:step]：产生新的对象'''
q='hello,Python'
q1=q[:5]
q2=q[6:]
q3='!'
new=q1+q3+q2
print(q1)
print(q2)
print(new)

'''格式化字符串
   1、%作为占位符
   2、{}作为占位符
   3、f-string'''

name='张三'
age=20
print('我叫%s，今年%d岁了' % (name,age))

print('我叫{0}，今年{1}岁了'.format(name,age))

print(f'我叫{name}，今年{age}岁了')

print('%d' % 99)
print('%10d' % 99) # 10表宽度
print('1111111111')

print('%f' % pi)
print('%.3f' % pi)
print('%10.3f' % pi) # 总宽度为10，小数点后保留三位

print('{:10.3f}'.format(pi))


