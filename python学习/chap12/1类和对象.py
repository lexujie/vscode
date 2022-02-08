'''
面向过程：事物比较简单，可以用线性的思维去解决
面向对象：事物比较复杂，使用简单的线性思维无法解决
'''

'''
类：多个类似事物组成的群体的统称（数据类型）
对象：一切皆对象
'''

'''
类的创建
'''

class Student:  # 类名可以为一个或者多个单词，每个单词首字母大写，其余小写
    native_place='吉林' # 类属性
    #
    def __init__(self,name,age):
        self.name=name
        self.age=age
    # 实例方法（在类之内定义的称为方法，在类之外定义的成为函数）
    def eat(self):
        print('学生在吃饭...')


    # 类方法
    @classmethod
    def cm(cls):
        print('类方法')

    # 静态方法
    @staticmethod
    def sm():
        print('静态方法')



# Student也为对象
print(id(Student))
print(type(Student))
print(Student)
print('-------------')

'''
对象的创建：类的实例化
实例名=类名（）
'''

stu1=Student('张三',20)
print(id(stu1))
print(type(stu1))
print(stu1)

stu1.eat()     # 对象名.方法()
print(stu1.name,stu1.age)

print('----------')

Student.eat(stu1) # 类名.方法(类的对象self)


'''类属性的使用方式'''
print(Student.native_place)
stu2=Student('李四',30)
print(stu1.native_place)
print(stu2.native_place)
Student.native_place='天津'
print(stu1.native_place)
print(stu2.native_place)
print('---------类方法的使用方式----------')
Student.cm()
print('---------静态方法的使用方式-------------')
Student.sm()
