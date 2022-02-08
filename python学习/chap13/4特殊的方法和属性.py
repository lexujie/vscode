'''
特殊属性
__dict__:获得类对象或实例对象所绑定的所有属性和方法的字典
'''

class A:
    pass
class B:
    pass
class C(A,B):
    def __init__(self,name,age):
        self.name=name
        self.age=age

# 创建C类对象
x=C('Jack',20)
print(x.__dict__) # 查看实例对象属性的字典
print(C.__dict__) # 查看类对象属性的字典
print('----------------')
print(x.__class__) # 输出对象所属的类
print(C.__bases__) # 输出父类的元素
print(C.__base__) # 输出第一个父类的元素
print(C.__mro__) # 类的层次结构
print(A.__subclasses__()) # 输出子类

'''
特殊方法
__len__():重写该方法，让内置函数len()的参数可以是自定义类型
__add__():重写该方法，可使用自定义对象具有+功能
__new__():用于创建对象
__init__():对创建的对象进行初始化
'''

a=20
b=100
c=a+b # 两个整数类型的对象的相加操作
d=a.__add__(b)
print(c)
print(d)

class Student:
    def __init__(self,name):
        self.name=name
    def __add__(self,other):
        return self.name+other.name
    def __len__(self):
        return len(self.name)

stu1=Student('张三')
stu2=Student('李四')
print(stu1+stu2) # 实现了两个对象的加法运算

print('----------------')
lst=[11,22,33,44]
print(len(lst)) # len是内容函数len
print(lst.__len__())
print(len(stu1))
print('------------')

class Person(object):

    def __new__(cls, *args,**kwargs):
        print('__new__被调用执行，cls的id值为{0}'.format(id(cls)))
        obj=super().__new__(cls)
        print('创建的对象的id为{0}'.format(id(obj)))
        return obj
    
    def __init__(self,name,age):
        print('__init__被调用了，self的id值为{0}'.format(id(self)))
        self.name=name
        self.age=age    

print('object这个类对象的id为{0}'.format(id(object)))
print('Person这个类对象的id为{0}'.format(id(Person)))

p1=Person('张三',20)
print('p1这个Person类的实例对象的id为{0}'.format(id(p1)))