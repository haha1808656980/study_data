'''
定义：就是可以使用for-in进行遍历，并且可以使用next依次获取元素的对象
说明：

- 生成器就是一种特殊的迭代器
- 判断是否是迭代器
- 字符串、列表、元组、集合、字典等都不是迭代器，他们都是可迭代对象。
- 任何实现了 __iter__ 和 __next__ 的方法的对象都是迭代器
	__iter__:返回迭代器自身
	__next__:返回容器的下一个值

优点：节省内存，惰性求值
'''
#自定义一个迭代器,实现斐波拉契数列
class Fib(object):
	"""docstring for Fib"""
	def __init__(self, max):
		self.x = x
		self.y = y
		self.max = max

	def __iter__(self):
		return self

	def __next__(self):
		n_next = self.y
		self.x,self.y = self.y,self.x+self.y
		if self.y < self.max:
			return n_next    #条件成立，返回下一个
		else:
			return StopIteration()          #不成立返回错误提示

#定义一个随机数迭代器
import random
class RandomShu(object):
	"""docstring for Fib"""
	def __init__(self, start,end,max_times):
		self.start = start
		self.end = end
		self.count = 0
		self.max_times = max_times


	def __iter__(self):
		return self

	def __next__(self):
		self.count+=1
		if self.count <= self.max_times:
			return random.randint(self.start,self.end)
		else:
			return StopIteration()          #不成立返回错误提示
r = RandomShu(1,50,30)


from collections import Iterator

l = (i for i in range(10))
print(isinstance(l, Iterator))  #判断是不是迭代器


'''
iter函数
作用：将可迭代对象转换为迭代器
'''

lt1 = [i for i in range(10)]
print(isinstance(lt1, Iterator))
lt2 = iter(lt1)
print(isinstance(lt2, Iterator))

#自定义迭代器