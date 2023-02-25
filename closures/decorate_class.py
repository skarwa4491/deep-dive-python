'''
    decorator from perspective of classes
'''

from datetime import datetime , timezone

def info(self): # this is not closure
    result = list()
    result.append('time {}'.format(datetime.now(timezone.utc)))
    result.append('id : {}'.format( hex(id(self)) ))
    result.append('class : {}'.format(self.__class__.__name__))
    for k , v in vars(self).items():
        result.append('{0}:{1}'.format(k,v))
    return result

def debug_info(cls):    
    cls.debug = info
    return cls
  
@debug_info
class Person:
    
    def __init__(self , name , year) -> None:
        self.name = name
        self.year = year
    
    def say_hi(self):
        return 'hello There';

p = Person('Swapnnil' , 1991)
print(p.debug())