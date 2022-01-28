# 程序的组织结构

'''顺序结构'''
# 中间没有任何的判断和跳转

# python所有对象都有一个布尔值（通过bool()获取）
print(bool(False))
print(bool(0))
print(bool(None))
print(bool(''))
print(bool(""))
print(bool([]))
print(bool(list()))
print(bool(()))
print(bool({}))
print(bool(set()))
# 其他对象的bool值均为True

'''选择结构（if）'''
# 单分支结构
money = 1000
s = int(input('请输入取款金额'))
if money >= s:
    money = money-s
    print('取款成功，余额为：',money)

# 双分支结构
# 判断奇偶
num = int(input('请输入一个整数'))
if num%2 == 0:
    print(num,'是偶数')
else:
    print(num,'是奇数')

# 多分支结构
score=int(input('请输入一个成绩：'))
if 90 <= score <= 100:
    print('A')
elif  80<= score < 90:
    print('B')
elif 70<= score < 80:
    print('C')
elif  60<= score < 70:
    print('D')
elif 0 <= score < 60 :
    print('E')
else:
    print('输入成绩不符合规范')

# 嵌套if
answer = input('您是会员吗？y/n')
money = float(input('购物金额为：'))
if answer == 'y':
    if money >= 200:
        print('应该收取金额',money*0.8)
    elif 100 <= money <200:
        print('应该收取金额',money*0.95)
    elif 0 < money < 100:
         print('应该收取金额',money)
    else:
        print('输入金额不合规范')
elif answer == 'n':
    if money >= 200:
        print('应该收取金额',money*0.95)
    elif 0 < money < 200:
        print('应该收取金额',money)
    else:
        print('输入金额不合规范')
else:
    print('无法确定是否为会员请重新输入')

# 条件表达式
a = int(input('请输入第一个整数'))
b = int(input('请输入第二个整数'))
print( str(a)+'大于等于'+str(b) if a >= b else str(a)+'小于'+str(b))
# 条件判断为True，执行左侧，否则执行右侧

'''pass语句'''
# 只是一个占位符，用在语法上需要语句的地方
answer = input('您是会员吗？y/n')
if answer == 'y':
    pass
else:
    pass
