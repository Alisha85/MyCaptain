#  Python Program for Fibonacci numbers.
def fib(n):

    a = 0
    b = 1

    if n == 0:
        print(a)
        
    elif n==1:        
        print(a)
        print(b)
    else:
        print(a)
        print(b)

    for i in range(2,n):
        c = a + b
        a = b
        b = c
        print(a+b)

fib(5)
