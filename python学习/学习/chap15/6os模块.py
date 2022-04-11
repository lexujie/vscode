'''os模块与操作系统相关的一个模块'''
import os
print(os.getcwd())
os.system('notepad.exe') # 打开记事本

# 直接调用可执行文件
os.startfile('C:\\Users\\HP\\AppData\\Local\\Programs\\Notion\\Notion.exe')