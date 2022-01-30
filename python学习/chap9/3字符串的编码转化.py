'''编码：将字符串转换位二进制数据(bytes)
   解码：将bytes类型的数据转化成字符串类型'''

s='天涯共此时'
print(s.encode(encoding='GBK')) # GBK：一个中文占两个字节
print(s.encode(encoding='UTF-8')) # GBK：一个中文占三个字节

byte=s.encode(encoding='GBK')
print(byte.decode(encoding='GBK'))