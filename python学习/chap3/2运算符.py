'''算术运算符
加（+）、减（-）、乘（*）、除（/）、整除（//,一正一负向下去整）
取余（%） 余数=被除数-除数*商 一正一负商为整除的结果
幂运算符（**）''' 

print(-9 % 4)
print(9 % -4)

'''赋值运算符
顺序从右到左'''

i = 3 + 4
print(i)

a=b=c=20 # 链式赋值
print(a,id(a))
print(b,id(b))
print(c,id(c))

a+=30 # 支持参数赋值 a = a + 30
print(a)
a*=2
print(a)
a/=3
print(a) # 变为float类型
a//=3
print(a)

# 支持系列解包赋值
a,b,c = 20,30,40 #等号左右两侧数量相等
print(a,b,c)

# 交换两个变量的值
a,b = 10,20
print('交换之前：',a,b)
a,b = b,a
print('交换之后：',a,b)

'''比较运算符:输出为bool类型
一个变量由id,type,value组成
其比较的是value'''

a,b = 10,20
print(a>b)
print(a<b)
print(a<=b)
print(a==b)
print(a!=b) # 不等号

# 比较id用is
a,b = 10,10
print(a==b)
print(a is b)
print(a is not b)

lst1 = [11,22,33,44]
lst2 = [11,22,33,44]
print(lst1 == lst2)
print(lst1 is lst2)
print(id(lst1))
print(id(lst2))


'''bool运算符：and,or,not,in,not in'''
a,b = 1,2
print(a==1 and b==2)
print(a==1 and b<2)

print(a==1 or b<2)

f1 = True
f2 = False
print(not f1)

s = 'helloworld'
print('w' in s)
print('k' not in s)

'''位运算符：将数据转成二进制进行计算'''

# 位与&：对应的数位都是1，结果位数才是1，否则为0

print(4 & 8) # 4二进制00000100，8二进制00001000

# 位或|：对应的数位都是0，结果位数才是0，否则为1

print(4 | 8) # 结果为00001100

# 左移位运算符<<：高位溢出舍弃，低位补0

print(4<<1)

# 右移位运算符>>：低位溢出舍弃，高位补0

print(8>>2)

'''运算优先级'''
# **
# *,/,//,%
# +,-
# <<,>>
# &
# |
# >,<,<=,>=,==,!=
# and
# or
# =