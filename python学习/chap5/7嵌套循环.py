# 嵌套循环：在循环结构中嵌套另外的循环

# 输出一个三行四列的矩形
for i in range(1,4):
    for j in range(1,5):
        print('*',end='\t') # 不换行输出
    print() # 换行

# 输出9*9乘法表
for i in range(1,10):
    for j in range(1,i+1):
        print(i,'*',j,'=',i*j,end='\t')
    print()


# 二重循环中的break和continue用于控制本层循环
for i in range(5):
    for j in range(1,11):
        if j%2==0:
            #break
            continue
        print(j)
