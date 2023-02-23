"""
    when used decorator , note function __name__ changes to inner function and doc strings
    wraps is itself a decorator
    
"""
from functools import wraps

counters = dict()

def counter(fn): # this is higher order function , which accepts function as parameter
    count = 0
    def inner(*args, **kwargs):
        nonlocal count
        count += 1
        counters[fn.__name__] = count       
        return fn(*args, **kwargs)
    return inner

def optimized_counter(fn):
    count =0
    def inner(*args, **kwargs):
        nonlocal count # free variable
        count+=1
        counters[fn.__name__] = count
        inner.__name__ = fn.__name__
        inner.__doc__ = fn.__doc__
        return fn(*args , **kwargs) # free variable
    return inner


def optimized_counter(fn):
    count =0
    @wraps(fn) # this is a decorator , which changes metadata
    def inner(*args, **kwargs):
        nonlocal count # free variable
        count+=1
        counters[fn.__name__] = count
        return fn(*args , **kwargs) # free variable
    return inner
        

@optimized_counter
def add(a,b):
    """_summary_
    sample doc string
    """
    return a+b;

add(10,20)