import sys
sys.setrecursionlimit(10**6)

def timed(fn):
    from time import perf_counter
    from functools import wraps
    @wraps(fn)
    def inner(*args , **kwargs):
        start = perf_counter()
        result =fn(*args , **kwargs)
        end = perf_counter()
        print('it took {} secs to execute {}'.format(end-start,fn.__name__))
        return result
    return inner

def fibonacci_recursion(n):
    if n<=2:
        return 1
    return (fibonacci_recursion(n-1) + fibonacci_recursion(n-2))

@timed
def fibonacci(n): # this function is to avaoid extra printing
    return fibonacci_recursion(n)

@timed
def fib_loop(n):
    fib1 = 1
    fib2 = 1
    for i in range(3,n+1):
        fib = fib1 + fib2 
        fib1 , fib2  = fib2 , fib
    return fib2

@timed
def _reduce(n):
    pass
    
        
output = fibonacci(40)
print(output)

output = fib_loop(40)
print(output)