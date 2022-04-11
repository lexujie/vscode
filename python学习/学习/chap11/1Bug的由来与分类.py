'''
Bug的常见类型：
1、粗心导致的语法错误 SyntaxError
2、知识不熟练导致的错误
3、思路不清导致的问题
4、被动掉坑
'''
# try 可能出现异常的代码 except 异常处处理代码
try:
    a=int(input('请输入第一个整数'))
    b=int(input('请输入第二个整数'))
    result=a/b
    print('结果为：',result)
except ZeroDivisionError:
    print('除数不能为0')
except ValueError:
    print('只能输入数字')

# try...except..else
try:
    a=int(input('请输入第一个整数'))
    b=int(input('请输入第二个整数'))
    result=a/b   
except BaseException as e:
    print('出错了')
    print(e)
else:
    print('结果为：',result)

# try...except...else..finally
# finally：无论是否异常都会执行，用来释放try中申请的资源
try:
    a=int(input('请输入第一个整数'))
    b=int(input('请输入第二个整数'))
    result=a/b   
except BaseException as e:
    print('出错了')
    print(e)
else:
    print('结果为：',result)
finally:
    print('谢谢您的使用')


'''
常见的异常：
1、ZeroDivisionError:除（或取模）零（所有数据类型）
2、IndexError：序列中没有此索引
3、Keyerror：映射中没有此索引（index）
4、NameError:未声明/初始化对象（没有属性）
5、SyntaxError:Python语法错误
6、Valuerror:输入无效参数
'''


'''traceback模块：打印异常信息'''
import traceback
try:
    print('1.------------')
    num=10/0
except:
    traceback.print_exc()
