'''增加操作'''
# 向列表的末尾添加一个元素
lst=[10,20,30]
print(lst,id(lst))
lst.append(100)
print(lst,id(lst))

# 向列表的末尾至少添加一个元素
lst2=['hello','world']
#lst.append(lst2)
lst.extend(lst2)
print(lst)

# 在列表的任意位置添加一个元素
lst.insert(1,90)
print(lst)

# 在列表任意位置添加N个元素
lst[1:]=lst2
print(lst)