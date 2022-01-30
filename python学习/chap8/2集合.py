# 集合：是没有value的字典，属于可变类型的序列

'''集合的创建方式'''
# 1、使用{}


s={2,3,4,5,5,6,7,7} #集合中的元素不能重复
print(s,type(s))

# 2、使用内置函数set()
s1=set(range(6))
print(s1,type(s1))

s2=set([1,2,3,3,5,6,5])
print(s2)

s3=set((1,2,3,45,43,23))
print(s3)

s4=set('python')
print(s4) # 集合中的元素是无序的

# 定义空集合
s5=set()
print(s5,type(s5))