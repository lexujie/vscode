'''remove()
   1、一次删除一个元素
   2、重复元素只删除第一个'''

lst=[10,20,30,10]
lst.remove(10)
print(lst)


'''pop()
   1、删除一个指定索引位置上的元素
   2、不指定则删除最后一个元素'''

lst.pop(1)
print(lst)
lst.pop()
print(lst)

'''切片
   一次删除多个元素，但是产生新的列表对象'''
lst2=[23,43,56,34,22]
lst3=lst2[1:3]
print(lst3)

# 不产生新的列表对象
lst2[1:3]=[]
print(lst2)

'''clear()
   清空列表'''

lst.clear()
print(lst)

'''del
   将列表删除'''
del lst2
print(lst2)