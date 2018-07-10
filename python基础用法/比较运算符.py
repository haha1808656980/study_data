'''
__eq__       等于
__ge__       大于等于 
__le__       小于等于
__gt__       大于
__lt__       小于
__ne__       不等于
'''
#完成一个类，实现负无穷的概念
class A(object):
	"""docstring for A"""
	def __le__(self,other):
		return True
	def __lt__(self,other):
		return True
	def __eq__(self,other):
		return False
	def __ge__(self,other):
		return False
	def __gt__(self,other):
		return False

