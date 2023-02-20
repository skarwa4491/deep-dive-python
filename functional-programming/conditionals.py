a = 2
if( a < 5):
    print(a)
else:
    print('if condition not met')
    
a = 20 
if(a < 5):
    print('a is less than 5')
elif(a < 10):
    print('a is less than 10')
elif(a < 50):
    print('a is less than 50')
elif(a < 30):
    print('a is less than 30')
else:
    print("where everything fails , this is executed")
    

def terneray(a):
    # x if(true) else y
    
    return True if(a<=5) else False

print(terneray(10))