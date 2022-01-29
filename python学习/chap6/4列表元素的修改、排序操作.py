'''修改'''
# 单个
lst=[10,20,30,40]
lst[2]=100
print(lst)
# 多个
lst[1:3]=[300,400,500,600]
print(lst)

'''排序sort()'''
lst2=[20,40,10,98,54]
print('排序前的列表：',lst2,id(lst2))
lst2.sort() # 开始排序，默认升序
print('排序后的列表：',lst2,id(lst2))

# 降序排序
lst2.sort(reverse=True)
print(lst2)


# 使用sorted()排序，将产生新的列表对象
lst3=[21,43,5654,3231,12]
print(lst3,id(lst3))
lst4=sorted(lst3)
print(lst4,id(lst4))

lst5=sorted(lst3,reverse=True)
print(lst5,id(lst5))

'''列表生产式'''
lst6=[i for i in range(1,10)]
print(lst6)
lst6=[i*i for i in range(1,10)]
print(lst6)