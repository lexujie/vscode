'''
python中的包
是一个分层次的目录结构，它将一组功能相近的模块组织在一个目录下

作用
代码规范、避免模块名称冲突

包与目录区别
包含__init__.py文件的目录称为包
目录里通常不包含__init__.py文件

包的导入
import 包名.模块名
'''
import pageage.module_A as ma
print(ma.a)