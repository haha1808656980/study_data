'''
dir方法和getattr的使用
'''
from datetime import datetime
print(dir(datetime))           #把对象的方法和属性全部打印出来
print('*'*50)
print(getattr(datetime,'ctime'))       #获取对象的属性
