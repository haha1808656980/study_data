'''
__enter__  进入with代码块前的操作
__exit__   退出时的善后操作

'''

#常用的地方

# 打开文件,不需要考虑文件的关闭
with open(file,'wb') as fp:
	fp.write()

#线程锁的使用
with lock

