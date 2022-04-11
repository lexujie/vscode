# continue:用于结束当前循环，进入下一次循环，通常与if一起使用

# 输出1-50所有5的倍数
for i in range(1,51):
    if i%5!=0:
        continue
    else:
        print(i)