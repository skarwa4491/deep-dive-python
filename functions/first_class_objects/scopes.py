def outer():
    x = 'hello'
    def inner():
        def inner2():
            print(x) # this will refer to x from non-local scope , as is not present in local function
        inner2()
    inner()
outer()

print('----------------------------- example2 -------------------------------------') 
def outer():
    x = 'hello'
    def inner():
        x = 'python' # this will create a new variable in local-scope
        print('inner' , x)
    inner()
    print('outer', x)
outer()

print('----------------------------- example3 -------------------------------------')
def outer():
    x = 'hello'
    def inner():
        nonlocal x
        x = 'python' # this will change the x from outer
    print('brefore inner ' , x)
    inner()
    print('after inner ', x)
outer()

print('----------------------------- example4 -------------------------------------')

def outer():
    x = 'hello'
    def inner():
        def inner2():
            nonlocal x 
            x = 'python' # this will change x from outer as x is not present in inner
        inner2()
    inner()
    print(x)

outer()
    
print('----------------------------- example5 -------------------------------------')

def outer():
    x = 'hello'
    def inner():
        nonlocal x
        x = 'python'
        def inner2():
            nonlocal x 
            x = 'monty' # non-local chaining
        print('before inner 2' , x)
        inner2()
        print('after inner 2' , x)
    inner()
    print(x)
    
outer()
print('----------------------------- example6 -------------------------------------')

x = 'python'

# def outer():
#     global x
#     x = 'monty'
#     def inner():
#         nonlocal x # this will not work , as outer contain global x , non local x
#         x = 'hello'
    
#     print(x)

print('----------------------------- example7 -------------------------------------')