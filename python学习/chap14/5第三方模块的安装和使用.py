'''
在终端中安装
pip install 模块名
pip install schedule
使用
import 模块名

'''
import schedule
import time
def job():
    print('哈哈--------')

schedule.every(3).seconds.do(job)
while True:
    schedule.run_pending()
    time.sleep(1)