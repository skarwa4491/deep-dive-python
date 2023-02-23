"""
A simple function timer , which returns the time to execute a function

"""
from ast import arg
import re
import time
from tracemalloc import start
from unittest import result


def time_it(fn, *args, rep=1, **kwargs):
    start = time.perf_counter()
    for i in range(rep):
        fn(*args, **kwargs)
    end = time.perf_counter()
    return (end-start)/rep


def compute_pow(n , *, start=1, end):
    return [n**i for i in range(start,end)]


print(time_it(compute_pow, 2 , end=20000, rep=1))
