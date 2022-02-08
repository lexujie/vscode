'''
class 子类类名(父类1,父类2...):
    pass
'''

class Person(object):# Person继承了object类
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def info(self):
        print(self.name,self.age)


class Student(Person):
    def __init__(self,name,age,stu_no):
        super().__init__(name,age)
        self.stu_no=stu_no
    def info(self):
        super().info()
        print(self.stu_no) #方法重写:可以通过super().xxx()调用父类中被重写的方法

class Teacher(Person):
    def __init__(self,name,age,teachyear):
        super().__init__(name,age)
        self.teachyear=teachyear
    

stu=Student('张三',20,'1001')
teacher=Teacher('李四',36,10)

stu.info()
print('-------------')
teacher.info()

'''
object类
是所有类的父类，因此所有类都有object类的属性和方法
'''

class Bank:
    def __init__(self,name,money):
        self.name=name
        self.money=money
    def __str__(self):
        return '我的名字是{0},我有{1}元'.format(self.name,self.money)

bank=Bank('张三',1000)
print(dir(bank))
print(bank)
