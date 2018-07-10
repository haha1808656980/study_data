# 使用type创建类

A = type('A',(object,),{})
print(type(A))
a = A()
print(a)
print('------------------------')
MyDict = type('MyDict',(dict,),{'length':10})
mydict = MyDict()
print(mydict.length)

