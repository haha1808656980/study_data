'''
定义：

- 外部函数中定义一个内部函数，
- 内部函数中使用了外部函数的变量，
- 外部函数将内部函数作为返回值返回。

'''

def wai(n):
    def nei():
        return n*n
    return nei

f1 = wai(3)   
print(f1)   #此时调用的只是外部函数，返回的是一个函数

print(f1()) #调用这个函数，给出返回值


def wai(a, b):
    def nei(x):
        return a*x + b
    return nei
f2 = wai(3, 5)  

print(f2(3)) 