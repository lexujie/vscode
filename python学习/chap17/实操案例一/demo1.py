
'''
输出的目的地是文件
一、使用print方式进行输出
'''
fp=open('E:\\OneDrive\\vscode\\python学习\\chap17\\实操案例一\\test.txt','w',encoding='utf-8')
print('横眉冷对千夫指',file=fp)
fp.close()

'''
二、使用文件读写操作
'''
with open('E:\\OneDrive\\vscode\\python学习\\chap17\\实操案例一\\test2.txt','w',encoding='utf-8') as file:
    file.write('俯首甘为孺子牛')