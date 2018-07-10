'''
Lambda函数又称匿名函数，
匿名函数就是没有名字的函数，函数没有名字也行？

当然可以啦。有些函数如果只是临时一用，而且它的业务逻辑也很简单时，
就没必要非给它取个名字不可
'''

print(lambda x, y : x+y)

#可以
list1 = [3,5,-4,-1,0,-2,-6]
print(sorted(list1,key=lambda x : abs(x)))  #求绝对值，从大到小排列

#也可以
add = lambda x,y : x + y
print(add(5,6))

'''结合map使用
说明：接受两个参数，一个函数和一个可迭代对象，
	 返回一个生成器，将func依次作用于lt
'''
print(list(map(lambda x: x*x,range(1,21))))


'''
结合reduce使用
 说明：接受两个参数，一个函数和一个可迭代对象，
 首先取两个元素，使用func处理，
 结果和第三个元素继续使用func处理，
 直到结束，返回处理的结果

'''
from functools import reduce
l = [1,2,3,4,5]
print(reduce(lambda x,y:x+y,range(1,21)))

'''
结合filter使用
使用func依次作用于每个元素，处理结果为True保留下来
'''
print(list(filter(lambda x:x%2==0,range(1,21))))