'''
为了解决内存突然增大问题，python引入了生成器

通过在函数中使用yield关键字

特性：

- 可以使用next获取数据，一次一个，结束时会报错
- 只能遍历一遍
- 可以转换为列表
- 可以使用for-in遍历

'''
l = [i for i in range(10)]  #列表生成式

l2 = (i for i in range(1,1000000)) #生成器

print(type(l))
print(type(l2)) 

#通过next获取
print(next(l2))
print(next(l2))
#使用 for in 遍历
for j in l2:
	pass

print('-----------------------------')

'''在函数中返回一个生成器，需要使用yeild的关键字'''

def test(n):
	for i in range(1,n+1):
		yield i

t = test(10000)
print(type(t))

#自定义一个生成器函数实现斐波拉契
def Fib(max):
	x = 0
	y = 1
	while y<max:
		yield y       #使用了yeild函数
		x,y = y,x+y


