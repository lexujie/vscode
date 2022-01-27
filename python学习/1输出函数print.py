#可以输出数字
print(520)

#可以输出字符串
print('helloworld')
print("helloworld")

#含有运算符的表达式
print(3+1)

#可以将数据输出文件中
#注：1、指定盘存在；2、使用file=
#'a+':如果文件不存在就创建，存在就文件内容后继续追加
fp=open('E:/OneDrive/vscode/python学习/text.txt','a+')
print('helloworld',file=fp)
fp.close()

#不进行换行输出
print('hello','world','python')