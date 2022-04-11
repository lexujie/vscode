'''函数：执行特定任务和完成特定功能的一段代码'''

'''创建：
def 函数名([输入参数])
    函数体
    [return xxx]'''

def calc(a,b): # a,b为形参，函数定义处
    c=a+b
    return c

'''调用'''
result=calc(10,20) # 10，20为实参，函数调用处
print(result)

res=calc(b=10,a=20)
print(res)

'''参数传递
   不可变对象修改不会影响
   可变对象修改会影响'''

def fun(arg1,arg2):
    print('arg1=',arg1)
    print('arg2=',arg2)
    arg1=100
    arg2.append(10)
    print('arg1=',arg1)
    print('arg2=',arg2)
    return

n1=11
n2=[22,33,44]
print('n1=',n1)
print('n2=',n2)
fun(n1,n2)
print('n1=',n1)
print('n2=',n2)

'''函数的返回值（没有返回值，可以省略return）
   函数返回是一个，直接返回原值
   函数的返回是多个值，结果为元组'''
def fun(num):
    odd=[]
    even=[]
    for i in num:
        if i%2:
            odd.append(i)
        else:
            even.append(i)
    return odd,even

print(fun([10,29,34,23,44,53,55]))

def fun1():
    return 'hello'

print(fun1())

def fun2():
    return 'hello','world'

print(fun2())



