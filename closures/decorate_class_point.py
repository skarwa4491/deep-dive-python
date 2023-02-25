from math import sqrt


def info(self):
    
    from datetime import datetime,timezone
    result = dict()
    result['time'] = datetime.now(timezone.utc)
    result['id'] = hex(id(self))
    result['class'] = self.__class__.__name__
    for k,v in vars(self).items():
        result[k]=v 
    return result

def __lt__(self,other):
        if isinstance(other , Point):
            return self.x < other.x and self.y < other.y
        return False
    
def __eq__(self,other):
    if isinstance(other , Point):
        return self.x < other.x and self.y < other.y
    return False
    
def __le__(self,other):
    if isinstance(other , Point):
        return self.x <= other.x and self.y <= other.y
    return False

def debug(cls):
    cls.debug = info
    return cls

def ordering(cls):
    cls.__le__ = __le__
    cls.__eq__ = __eq__
    cls.__lt__ = __lt__
    return cls

@ordering
@debug
class Point:
    """_summary_
    
    1. __gt__ , __le__ , __ge__ there is no need to implement this as
    __lt__ and __eq__ is implemented
    __gt___ is compliment of __lt__ and this is automatically managed py python
    
    """
    
    def __init__(self , x , y) -> None:
        self.x = x
        self.y = y
    
    def __abs__(self , x ,y): # this is called when we call absolute value abs
        return sqrt(self.x**2 + self.y**2)

    def __repr__(self) -> str:
        return 'Point x:{}, y:{}'.format(self.x , self.y)
    
    
point1 , point2 , point3 = Point(10,20) , Point(10,20) , Point(2,3)
print(point3 > point1)
print(point1== point2)
print(point1 <= point2)
print(point1.debug())
print(point2.debug())
print(point3.debug())
