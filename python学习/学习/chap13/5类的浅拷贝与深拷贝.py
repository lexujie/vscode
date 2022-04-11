'''
浅拷贝：拷贝时，对象包含的子对象内容不拷贝，因此，源对象与拷贝对象会引用同一子对象

深拷贝：使用copy模块的deepcopy
递归拷贝对象中包含的子对象，源对象和拷贝对象所有的子对象也不同
'''

class CPU:
    pass
class Disk:
    pass
class Computer:
    def __init__(self,cpu,disk):
        self.cpu=cpu
        self.disk=disk

# 变量的赋值
cpu1=CPU()
cpu2=cpu1
print(cpu1)
print(cpu2)

# 类的浅拷贝
disk=Disk()
print(disk)
computer=Computer(cpu1,disk)

import copy
computer2=copy.copy(computer)
print(computer,computer.cpu,computer.disk)
print(computer2,computer2.cpu,computer2.disk)
print('----------------------')

# 深拷贝
computer3=copy.deepcopy(computer)
print(computer3,computer3.cpu,computer3.disk)
