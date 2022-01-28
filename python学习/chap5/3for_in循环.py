'''for_in循环
   in表达从字符串、序列中依次取值，称为遍历'''

for item in 'Python':
    print(item)

for i in range(1,10,2):
    print(i)

# 如果在循环体中不需要使用到自变量，可以自定义变量写为 _
for _ in range(5):
    print('I love you')

# 计算1-100的偶数和
sum=0
for a in range(1,101):
    if a%2==0:
        sum+=a
print(sum)

# 输出100-999的水仙花数
# 个、十、百位上的数的三次方相加的和相等
for i in range(100,1000):
    ge=i%10
    shi=i//10%10
    bai=i//100
    if ge**3+shi**3+bai**3==i:
        print(i)
