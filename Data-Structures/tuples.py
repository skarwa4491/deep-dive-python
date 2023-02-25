'''
   1. Tuples vs list vs strings
   2. () this does not creates a tuple , does although this is also important
   3. _ variable name is a pythin way to store something on varibale , which will never be used
   4. tuples are immutable , but if we have a tuple of mutable objects , then values of tuple can be changed
'''

address = 'Aurangabad', 'SambhajiNagar', 'Maharashtra', '431001'
print(address)

print(address[0])

city, *_, pincode = address  # this is extended unpcaking
print(city)
print(pincode)
print(_)


class Point2D:

    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
    
    def __repr__(self) -> str:
        return f'{self.__class__.__name__ }(x={self.x} , y={self.y})'

pt = Point2D(10,20)
print(pt)

tup = (Point2D(20,30) , Point2D(30,40))
print(tup)
tup[0].x = 50
print(tup)