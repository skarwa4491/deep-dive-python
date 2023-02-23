'''
    parameterized decorators
'''
def timed_factory(reps):
    def timed(fn):
        from time import perf_counter
        def inner(*args , **kwargs):
            total_elapsed = 0
            for i in range(reps):
                start = perf_counter()
                result = fn(*args , **kwargs)
                end = perf_counter()
                total_elapsed += (end-start)
            _average = total_elapsed / reps
            print('average run time is {0:.6f} for {1} reps'.format(_average , reps))
            return result
        return inner
    return timed


def myfunc(n):
    if n < 3:
        return 1
    return myfunc(n-2)+ myfunc(n-1)


@timed_factory(10)
def fib_n(n):
    return myfunc(n)

print(fib_n(10))