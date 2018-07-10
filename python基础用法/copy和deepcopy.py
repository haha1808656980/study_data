
'''赋值引用 is 、==、copy、deecopy'''
# def extendList(val,list=[]):
# 	list.append(val)
# 	return list
# list1 = extendList(10)         #结果[10, 'a']
# list2 = extendList(123,[])     #结果[123]
# list3 = extendList('a')        #结果[10, 'a']
# print(list1,list2,list3)

from copy import copy,deepcopy
from pickle import dumps,loads

a = [1,2,3]
b = [a] * 3
c= copy(b)       
d = deepcopy(b)
e = loads(dumps(b,4))

b[1].append(999)
c[1].append(999)
d[1].append(999)
e[1].append(999)


print(b)       
print(c)              #b和c的执行结果都是[[1, 2, 3, 999, 999], [1, 2, 3, 999, 999], [1, 2, 3, 999, 999]]

print(d)
print(e)              #d和e的执行结果都是[[1, 2, 3, 999], [1, 2, 3, 999], [1, 2, 3, 999]]

#自定义deepcopy
my_deepcopy = lambda item:loads(dumps(item,4))
#总结：
# 1、copy属于浅拷贝，deepcopy属于深拷贝，
# 2、copy只拷贝父对象，不会拷贝对象的内部的子对象，父对象增加了，copy的对象也会增加
# 3、deepcopy完全复制然后变成一个新的对象，复制的对象和被复制的对象没有任何关系，彼此之间无论怎么改变都相互不影响。

#