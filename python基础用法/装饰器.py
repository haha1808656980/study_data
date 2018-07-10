'''
作用：提高代码的复用度

- 作用：当我们想要增强原来已有函数的功能，但不想(无法)修改原函数，可以使用装饰器解决

- 什么是装饰器：

  - 就是一个函数，该函数接受一个函数作为参数，返回一个闭包，而且闭包中执行传递进来的函数，闭包中可以在函数执行的前后添加一些内容。

'''

'''无参数'''
	def show(func):
	def run():
		print('good  boy')
		func()
		print('yeah!')
	return run

@show
def Nice():
	print('二货')

Nice()     #在原有的基础上增加功能
print('--------------------')

'''有参数'''
def magic(func):
	def run(*args,**kwargs):
		print('嘿嘿')
		func(*args,**kwargs)
	return run

@magic
def test(n):
	print(n*n)

test(3)

print('------------------------')

'''有返回值的装饰器'''
def Perfect(func):
	def run(*args,**kwargs):
		return func(*args,**kwargs) *1000
	return run


@Perfect
def come(x,y):
	return x+y

print(come(3,5))