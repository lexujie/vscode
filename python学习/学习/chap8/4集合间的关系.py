'''相等'''
s={10,20,30,40}
s1={30,10,20,40}
print(s==s1)
print(s!=s1)

'''子集'''
s2={10,20}
print(s2.issubset(s1))
print(s1.issubset(s2))

'''超集'''
print(s.issuperset(s2))

'''交集'''
print(s2.isdisjoint(s))  # 判断是否没有交集

'''得到集合的交集(相关集合无变化)'''
print(s2.intersection(s))
print(s2 & s)

'''得到集合的并集（相关集合无变化）'''
print(s2.union(s))

'''得到差集（相关集合无变化）'''
print(s.difference(s2))

'''得到对称差集'''
s3={10,40,50,60}
print(s3.symmetric_difference(s))

'''集合生成式'''
s4={i*i for i in s}
print(s4)