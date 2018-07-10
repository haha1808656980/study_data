'''
method: 通过实例调用时，可以引用类内部的任何属性和方法

classmethod: 无需实例化，可以调用类属性和类方法，无法取到类内部的属性方法

staticmethod:无论用类调用还是用实例调用，都无法取到类内部的属性和方法，完全独立的一个方法

'''

class Test(object):
	x = 123
	def __init__(self):
		self.y = 456
	def bar1(self):
		print("hello world")
	@classmethod
	def bar2(cls):
		print('bad wOrld')

	@staticmethod
	def bar3():
		print('======')
	def fool(self):
		print(self.x)
		print(self.y)
		self.bar1()
		self.bar2()
		self.bar3()
	@classmethod
	def foo2(cls):
		print(cls.x)
		print(cls.y)         #结果报错，可以调用类属性和类方法，但是无法取到类内部的属性方法
		cls.bar1()
		cls.bar2()
		cls.bar3()
	@staticmethod
	def foo3(obj):              #结果报错，缺少参数，成为完全独立的一个方法，无法被类调用
		print(obj.x)
		print(obj.y)
		obj.bar1()
		obj.bar2()
		obj.bar3()
t = Test()
t.fool()
t.foo2()
t.foo3()

