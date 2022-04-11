'''递归函数：在函数的函数体内调用了该函数本身（占用内存多，效率低）'''
def fac(n):
    if n==1:
        return 1
    else:
        return n*fac(n-1)

print(fac(6))

'''斐波那契数列'''
def fib(n):
    if n==1:
        return 1
    elif n==2:
        return 1
    else:
        return fib(n-1)+fib(n-2)

for i in range(1,11):
    print(fib(i),end=' ')
