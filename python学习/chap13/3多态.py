'''
多态：即便不知道一个变量所引用的对象到底是什么类型，仍然可以通过这个变量调用方法
在运行过程中根据变量所引用对象的类型，动态决定调用哪个对象中的方法
'''

class Animal(object):
    def eat(self):
        print('动物会吃')
class Dog(Animal):
    def eat(self):
        print('狗吃骨头')
class Cat(Animal):
    def eat(self):
        print('猫吃鱼')
class Person(object):
    def eat(self):
        print('人吃五谷杂粮')

def fun(obj):
    obj.eat()

fun(Dog())
fun(Cat())
fun(Person())