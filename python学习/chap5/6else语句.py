# else与while和for搭配使用时，没有碰到break，循环正常结束则执行else

for i in range(3):
    pwd=input('请输入密码')
    if pwd=='8888':
        print('密码正确')
        break
    else:
        print('密码错误')
else:
    print('三次密码均输入错误')
