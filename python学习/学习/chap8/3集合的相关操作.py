'''判断'''
s={10,20,30,40,50}
print(10 in s)
print(100 not in s)

'''新增'''
# 添加一个add()
s.add(80)
print(s)
# 添加多个upadate()
s.update({200,900,405})
print(s)
s.update([1,2,3,4])
print(s)

'''删除'''
# 删除一个指定的元素remove()，该元素不存在，则错误
s.remove(900)
print(s)
# s.remove(500)

# 删除一个指定的元素discard()，该元素不存在，不产生错误
s.discard(500)
# 删除一个任意元素pop()
s.pop() # 不能添加参数
print(s)
# 清空集合clear()
s.clear()
print(s)