def logged(fn):
     from functools import wraps
     from datetime import datetime , timezone
     
     @wraps(fn)
     def inner(*args, **kwargs):
         run_dt = datetime.now(timezone.utc)
         result = fn(*args , **kwargs)
         print('{0} : called {1}'.format(run_dt , fn.__name__))
         return result
     return inner


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


@logged # logged(timed(factorial))
@timed
def factorial(n):
    fact = 1
    for n in range(n,0,-1):
        fact *= n
    return fact

print(factorial(5))
