"""_summary_

    when we provide a default value to a arguments then, every argument after that 
    should also have a default value (OR) 
    parameter with default value should last in serries of arguments in function
    
    while calling a function , if we provide a keyword argument , then all following argument should 
    be keyword argument
    
"""


def func(a,b):
    return (a,b)

def default_value(a, b=100 , c=10): # b is last in serries
    return (a,b,c)

def default_multiple(a, b=10 , c=20): # b and c both have default values
    pass

print('positional argument ',func(10,20)) # called with positional arguments

print('keyword arguments' ,func(b = 40 , a = 10)) # called with keyword argument

print(default_value(1 , c=300 , b=900)) # mix and match of both positional and keyword arguments

print(default_value(10)) # take b as default value
print(default_value(80 , 700))
