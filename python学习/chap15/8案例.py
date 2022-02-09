# 列出指定目录下所有.py文件


import os
os.chdir('E:\\OneDrive\\vscode\\python学习\\chap15')
path=os.getcwd()
lst=os.listdir(path)
for filename in lst:
    if filename.endswith('.py'):
        print(filename)



os.chdir('E:\\OneDrive\\vscode\\python学习')
path1=os.getcwd()
lst_files=os.walk(path1) # 遍历指定文件下所有的文件和目录
for dirpath,dirname,filename in lst_files:
    '''
    print(dirpath)
    print(dirname)
    print(filename)
    print('-----------------')
    '''
    for dir in dirname:
        print(os.path.join(dirpath,dir))
    print('---------------')
    for file in filename:
        print(os.path.join(dirpath,file))
