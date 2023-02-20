'''
    Semantics
    
    def func(a,b):
        pass
    
    here 'a' and 'b' are parameters to a function,
    also 'a' and 'b' are local variables to a function
    these are pass by refrence
    
    func(x,y) -> here x and y are arguments , which are pass by refrence
'''


def func(a, b):
    print(id(a))
    print(id(b))


a = 10
b = 10
print('ouside a function')
func(a,b)
