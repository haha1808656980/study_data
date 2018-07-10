def fib(n):
	if n <= 2:
		return 1
	else:
		return fib(n-1)+fib(n-2)

fib=lambda n:1 if n<=2 else fib(n-1)+fib(n-2)

print(fib(10))


#求阶乘
def jie_cheng(x):
    if x==1:
        return 1
    elif x>1:
        return jie_cheng(x-1)*x
print(jie_cheng(5))