#计算一个数组的深度

class ClassName(object):
	"""docstring for ClassName"""
	def __init__(self, a):
		self.data =data
	def has_left(self,):
		pass

	def left(self,i):
		return self.data[2*i+1]
	def (self,i):
		return self.data[2*i+2]

	def deep_cal(a):
		deep=0
		length=len(a)
		all_items = 0
		while True:
			level_items = 2**deep
			all_items += level_items
			if length > all_items:
				deep += 1
			else:
				break
		return deep


	def get_level_item(self,level):
		i=level-1
		start=0
		while i>0:
			start+=2**(i-1)
			i-=1
		# start = 2**(3-1)+2**(3-2)+2**(3-3)
		# end = 2**(3)+2**(3-1)+2**(3-2)+2**(3-3)
			end = 2**(level-1) + start
		return start,end

	def sort(self):
		while len(self.data) > 1:
		 	deepath = self.deep_cal()
		 	#从第几层开始
		 	start_level =deepath -1 
		 	while start_level > 0:
		 		start,end =


