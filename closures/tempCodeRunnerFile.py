class MyClass:
    
    def __init__(self, a , b) -> None:
        self.a = a
        self.b = b
    
    def __call__(self,fn):
        def inner(*args , **kwargs):
            print('decorated by class with params a={}, b={}'.format(self.a,self.b))
            return fn(*args , **kwargs)
        return inner
        
    
@MyClass(10,20)
def my_func(s):
    print('hello {}'.format(s))

my_func('world')