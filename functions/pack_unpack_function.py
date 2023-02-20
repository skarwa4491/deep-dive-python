'''
     here * it will convert everything in tuple
     we cannot pass positional arguments, after *args
     
     
'''
def unpack(a, b, *c):
    print(a, b, c)

def unpack2(a,b,c):
    print(a,b,c)

def avg(*args):
    count = len(args)
    total = sum(args)
    if count == 0:
        return 0
    else:
        return total/count
    return count and total/count

unpack(10, 20, 30, 40, 50)
#unpack2([1,2,3]) # this is not allowed
unpack2(*[1,2,3]) 
print(avg(2,2,2))

