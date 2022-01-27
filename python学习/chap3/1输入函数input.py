# input：接收来自用户的输入

present = input('大圣想要什么礼物呢?')
print(present,type(present))

a = input('请输入一个加数')
b = input('请输入另一个加数')
print(type(a),type(b))
print(a + b) #str类型，+起连接作用
print(int(a)+int(b))

c = int(input('请输入一个加数'))
d = int(input('请输入另一个加数'))
print(c + d)