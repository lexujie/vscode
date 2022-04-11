'''
语法规则
file=open(filename,mode,encoding)
'''
file=open('E:/OneDrive/vscode/python学习/chap15/a.txt','r',encoding='UTF-8')
#print(file.readlines())
print(file.read())
file.close()

file=open('E:/OneDrive/vscode/python学习/chap15/b.txt','w',encoding='UTF-8')
file.write('helloworld')
file.close()

src_file=open('E:/OneDrive/vscode/pictures/git工作流.png','rb')
target_file=open('E:/OneDrive/vscode/python学习/chap15/copy.png','wb')
target_file.write(src_file.read())
target_file.close()
src_file.close()