# break:用于结束循环结构，通常与分支结构if一起使用

# 密码最多录入3次
for i in range(3):
    pwd=input('请输入密码')
    if pwd=='8888':
        print('密码正确')
        break
    else:
        print('密码错误')

a=0
while a<3:
    pwd=input('请输入密码')
    if pwd=='8888':
        print('密码正确')
        break
    else:
        print('密码错误')
