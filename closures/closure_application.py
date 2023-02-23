from time import perf_counter


counters = dict()

def averageer():
    numbers =[]
    def add(number):
        numbers.append(number)
        total = sum(numbers)
        count = len(numbers)
        return total/count
    return add

print('----------------------------- example 2 ------------------------------')

def timer():
    start = perf_counter()
    #time.sleep(5)
    def poll():
        return perf_counter() - start
    
    return poll

t1 = timer()
print(t1())

print('----------------------------- example 3 ------------------------------')

def counter(init_value):
    
    def inc( incrementer):
        nonlocal init_value
        init_value+= incrementer
        return init_value
    return inc

c = counter(10)
print(c(1) , c(1))

print('----------------------------- example 4 ------------------------------')

def counter(fn): # counts , ow many times a function is called
    count = 0
    def inner(*args , **kwargs):
        nonlocal count
        count+=1
        counters[fn.__name__] = count
        return fn(*args , **kwargs)
    return inner

def add(a , b):
    return a+b

def mult(a , b):
    return a*b

print(add.__closure__)
add = counter(add)
print(add.__closure__)
add(2,3)
print(counters)