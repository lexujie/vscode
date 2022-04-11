'''
默认参数：函数定义时，给形参设置默认值，只有与默认值不符的时候才需要传递实参
'''
def fun(a,b=10):
    print(a,b)

fun(100)
fun(20,30)

'''
个数可变的位置参数
使用*定义，结果为元组
'''
def fun(*args): # 只能定义一个
    print(args)

fun(10)
fun(10,20,30)

'''
个数可变的关键字形参
使用**定义，结果为一个字典
'''
def fun(**args): # 只能定义一个
    print(args)
fun(a=10)
fun(a=10,b=20,c=30)

def fun1(*args1,**args2): # 只有这种形式不报错
    pass

'''
*可以将列表中的元素转化为位置实参
**将字典中的元素转化为关键字实参
'''

def fun(a,b,c):
    print(a,b,c)

lst=[11,22,33]
fun(*lst)

dic={'a':100,'b':20,'c':300}
fun(**dic)

def fun(a,b,*,c,d): # 从*之后的只能采用关键字参数传递
    return
