def fib(n):
    a,b = 0,1
    for i in range(1,n):
        a,b = b,a+b
    return b

print(fib(3))
print(fib(5))
print(fib(7))