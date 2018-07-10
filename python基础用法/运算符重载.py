'''
__add__     加
__sub__     减
__mul__     乘
__mod__     除
'''

#实现字典的__add__方法，作用相当于d.update(other)
class D(object):
	"""docstring for ClassName"""
	def __add__(self, arg):
		if isinstance(self,other):
			new = deepcopy(self)
			new.update(other)
			return new
		else:
			raise TypeError('not a dict')