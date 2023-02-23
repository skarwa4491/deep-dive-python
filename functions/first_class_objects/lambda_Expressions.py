"""
    __summary__
    
    lambda expressions : function which does not have name are called as lamdbda functions
    they are also called as anonymous functions
    syntax:
    
    lambda [parameter list] : expression
    
    expression is evaluated and returned as a function object
    
    lamda funcitons are not closer
    
    limitations:
        cannot do assignments 
        cannot do annotations
        
"""
greet = lambda : 'hello i am lambda expression'

raise_power = lambda x : x**2

add = lambda x,y : x*y

reverse_and_change_caps = lambda s : s[::-1].upper()

dictionary = lambda **kwargs : kwargs

lamda_with_default_value = lambda s="abc": "default" if(s=="abc") else s[::-1]
# applications 

complex = lambda x , y , *args , d , **kwargs : (x,y,args,d,kwargs)

def apply_function(x , fn):
    return fn(x)

result = apply_function(4 , lambda x: x**2) # passing a lambda function as a parameter
print(result)

print(complex(10 , 20 , 30 ,40 , d=90 , e=80 , f=70))

