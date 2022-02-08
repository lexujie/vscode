'''
面向对象的三大特征：
封装：提高程序的安全性
继承：提高代码的复用性
多态：提高程序的可扩展性和可维护性
'''

'''
封装：将数据（属性）和行为（方法）包装到类对象中。
在方法內部对属性进行操作，在类对象的外部调用方法。这样，无需关心方法内部的具体实现细节，
从而隔离了复杂度。
在Python中如果该属性不希望在类对象外部被访问，前面使用两个_
'''

class Student:
    def __init__(self,age):
        self.set_age(age)
    def get_age(self):
        return self.__age
    def set_age(self,age):
        if 0<=age<=120:
            self.__age=age
        else:
            self.__age=18

stu1=Student(150)
stu2=Student(30)
print(stu1.get_age())
print(stu2.get_age())