'''
局部变量
在函数内定义，只在函数内部有效
使用global声明可以变成全局变量
'''
def fun(a,b):
    c=a+b
    print(c)

# print(c)

def fun():
    global c
    c=20
    
fun()
print(c)
'''
全局变量
函数外定义，可以作用函数内外
'''
name='乐许杰'
print(name)
def fun2():
    print(name)

fun2()