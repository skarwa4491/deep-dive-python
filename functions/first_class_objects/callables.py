"""_summary_
    callable is any object which is called with ()
    callable function returns boolean value if function is callable
    if something is callable , it will always return something, default is None
"""

print(callable(list))

class MyClass:
    
    def __init__(self , x=0) -> None:
        print('initializing')
        self.counter = x
        
    def __call__(self , x):
        print('updating counter')
        self.counter += x

print(callable(MyClass))

my_class = MyClass(100)
print(my_class.counter)
my_class(100)
print(my_class.counter)
MyClass.__call__(my_class , 10)
print(my_class.counter)
print(callable(my_class))