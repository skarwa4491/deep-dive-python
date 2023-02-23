"""_summary_
    specific --> may have default values
    *args --> collects and exhausts remaining positional arguments
    * --> exhausts positional arguments , will put them in tuple , refuse to accept positional arguments
    **kwargs --> must pass argument as key value pair
    
    a,b,c=10 --> all positional with c as default value
    if there default value before *args , we cannot use the default value , so a big BEAWARE
    
"""

def func(a , b=10 ,*args , c=20 , d=100 ):
    print(a , b, args ,c, d)
    
func(10 , 20 ,30 , 30 , d=20)
