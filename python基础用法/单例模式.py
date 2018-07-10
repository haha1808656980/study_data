'''
说明：这种模式涉及到一个单一的类，该类负责创建自己的对象，同时确保只有单个对象被创建。
这个类提供了一种访问其唯一的对象的方式，可以直接访问，不需要实例化该类的对象。

注意(1):单例类只能有一个实例。
	(2):单例类必须自己创建自己的唯一实例。
	(3):单例类必须给所有其他对象提供这一实例。


例子：
1、一个党只能有一个主席。
2、Windows 是多进程多线程的，在操作一个文件的时候，
 就不可避免地出现多个进程或线程同时操作一个文件的现象，
 所以所有文件的处理必须通过唯一的实例来进行。
3、一些设备管理器常常设计为单例模式，比如一个电脑有两台打印机，
  在输出的时候就要处理不能两台打印机打印同一个文件。

优点：
 1、在内存里只有一个实例，减少了内存的开销，尤其是频繁的创建和销毁实例（比如管理学院首页页面缓存）。
 2、避免对资源的多重占用（比如写文件操作）。
 3、单例模式可以控制单例数量；可以进行有意义的派生；对实例的创建有更自由的控制;
缺点：
没有接口，不能继承，与单一职责原则冲突，
一个类应该只关心内部逻辑，而不关心外面怎么样来实例化
'''

'''使用元类（metaclass）实现单例模式'''
class Singleton(type):
	"""docstring for Singleton"""
	def __init__(cls,name,bases,dict):
	
		super(Singleton, cls).__init__(name,bases,dict)
		cls.instance = None
	def __call__(cls,*args,**kw):
		if cls.instance is None:
			cls.instance = super(Singleton,cls).__call__(*args,**kw)
		return cls.instance

class MyClass(object):
	"""docstring for MyClass"""
	__metaclass__ = Singleton


#使用装饰器实现单例模式

def Singleton(cls):
	instances = {}
	def getinstance(*args,**kw):
		if cls not in instances:
			instances[cls] = cls(*args,**kw)
		return instances[cls]
	return getinstance

@Singleton
class MyTwoClass(object):
	"""docstring for MyTwoClass"""
	def __init__(self,name,age,sex):
		self.name = name
		self.age = age
		self.sex = sex

	def run(self):
		return self.name , self.age ,self.sex

c1 = MyTwoClass('bob',18,'男')
c2 = MyTwoClass('bob',18,'男')

print(c1 is c2)
print(c1)
print(c2)

'''使用__new__方法实现单例模式'''

class Singleton1(object):
	""" # 关键在于这，每一次实例化的时候，
	我们都只会返回这同一个instance对象"""
	#hasattr 表示有属性
	def __new__(cls):
		if not hasattr(cls,'instance'):
			cls.instance = super(Singleton1,cls).__new__(cls)
		return cls.instance

obj1 = Singleton1()
obj2 = Singleton1()

obj1.attr = 'value1'
obj2.attr = 'value2'
#会发现obj1和obj2始终是一致的，说明实现单例化
print(obj1.attr)
print(obj2.attr)









		