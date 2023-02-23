"""
    forcing the user to have named arguments 
    after positional arguments, when given *, we exhaust all positional arguments 
    and any arguments after that are mandatory named arguments
"""

def force_named(a,b,*args,d):
    print(a,b,args,d)

def named(*args,d):
    print(args,d)

def func(*,d): # *args is end of positioinal arguments
    print(d)

def at_least_two(a,b,*args,d,e=True): # here at leaset two positiinal args are expected
    pass

def at_most_two(a,b,*,d,e=True): # here at most 2 positional args are expected
    pass

force_named(1,2,'x','y',d=100)
force_named(1,2,d=100) # args are empty tuple
#force_named(1,2) # this will give error

named(d=100) # args are empty
named(1,2,3,d=100)
#func(1,2,3) # 0 positional args are expected , but 3 were given
func(d=100)

print('##############################################################################################')

def func1(a,b,c):
    pass

func1(1, b=10 , c=10) # onece you provide keyword args , all args after that should be provided, as keyword args

# when we give default value to a positional argument, all positional arguments after that should have a default value 
# except * args ,well that is not the case for keyword arguments
def mix_n_match(a, b=4, *args , d):
    print(a,b,args,d)

def mix_n_match_2(a,b,*args,d=5,c):
    print(a,b,args,d,c)
    
mix_n_match(1,5,7,6,5,d=8)
mix_n_match_2(5,4,8,9,0,d=8,c=9)
mix_n_match_2(5,4,8,9,0,c=9)