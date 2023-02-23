"""
    closures:
    
    1. inner function creation doest not happen until outer is called
    x of outer and x of inner are same 
    the non local variables from inner is also called as free variable
    
    2. when inner function uses variable from non local scope is called closure
    3. when we return an inner function , we infact return a closure 
    because we return function which is using non local variable
    4. when we return a closure, a new object cell is created, which points to non
    local variable from outer function
    5. when there is a shared variable between two different scopes and new object cell is
    created , which points to shared variable
"""
from itertools import count
from time import process_time_ns


def outer():
    x = 'python'

    def inner():
        print('{} rocks '.format(x))
    return inner


inner = outer()  # inner will be created now , when outer is called
inner()

print('-------------------------------- example 2------------------------------')


def outer():
    x = 'python'
    print(hex(id(x)))

    def inner():
        print(hex(id(x)))
        print(x)
    return inner


fn = outer()
print(fn.__closure__)
fn()

print('-------------------------------- example 3 ------------------------------')


def outer():
    a = 100
    x = 'python'
    print('outer x id ', hex(id(x)))

    def inner():
        a = 10  # this is not free variable
        print('inner x id ', hex(id(x)))
        print('{} rocks !'.format(x))  # this is a non-local or a free variable
    return inner


fn = outer()
print(fn.__code__.co_freevars)  # this will list all free variables
print(fn.__closure__)  # this retugrn cell object pointing to gree variable
fn()

print('-------------------------------- example 4 ------------------------------')


def outer():
    x = 100

    def inner():
        nonlocal x  # modifying non local variable
        x += 1
        return x
    return inner


fn = outer()
print(fn.__code__.co_freevars)
print(fn())
print(fn())

print('-------------------------------- example 5 ------------------------------')
# multiple instances of closures


def outer():
    x = 100

    def inner():
        nonlocal x  # modifying non local variable
        x += 1
        return x
    return inner


# two diff closure
f1 = outer()
f2 = outer()
print(f1(), f1())
print(f2(), f2(), f2())
print(f1(), f1(), f1())

print('-------------------------------- example 6 ------------------------------')
# share extended scopes

def outer():
    x = 10 
    def inner1():
        nonlocal x
        x+=1
        return x
    
    def inner2(): 
        nonlocal x
        x+=1
        return x
    return inner1 , inner2 # return shared closure , as both clsures are refering to same x

fn1 , fn2 = outer()
print(fn1() , fn2() , fn2() , fn2() , fn1())

print('-------------------------------- example 7 ------------------------------')

def outer(n):
    def inner(x):
        return x+n
    return inner
fn1 = outer(1)
fn2 = outer(2)
fn3 = outer(3)

print(fn1(1) , fn2(2) , fn3(3))

print('-------------------------------- example 8 ------------------------------')

adders = []
for n in range(1,4):
    adders.append(lambda x : x+n) # this is closure with lambda

for add in adders:
    print(add(10))
    
print('-------------------------------- example 9 ------------------------------')
# nested closures

def outer(n):
    def inner(start):
        current = start
        def inc():
            nonlocal current
            current += n
            return current
        return inc
    return inner

inner = outer(10)
print(inner.__code__.co_freevars)
inc = inner(1)
print(inc() , inc() , inc())
print('free variables' , inc.__code__.co_freevars)
    
        
