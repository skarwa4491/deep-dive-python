from tkinter import Widget


class Rectangle:
    
    def __init__(self , height , width) -> None:
        self.height = height
        self.width = width
    
    @property # getter
    def width(self):
        return self._width
    
    @width.setter
    def width(self , width):
        if width <= 0:
            raise ValueError(' width should be positive')
        else:
            self._width = width
    
    @property
    def height(self):
        return self._height
    
    @height.setter
    def height(self , height):
        if height <= 0:
            raise ValueError(' height should be positive')
        else:
            self._height = height
    
    def __str__(self) -> str:
        return 'rectange height={} , width={}'.format(self._width , self._height)

    def __eq__(self, other):
        if isinstance(other, Rectangle):
            return (self._height == other._height and self._width == other._width)
        else:
            return False
    
    def __repr__(self) -> str:
        return 'Rectangle({} , {})'.format(self._height,self._width)
    
    
r = Rectangle(100,10)
r1 = Rectangle(100,10)
r2 = Rectangle(90,10)
print(r1 == r)
print(r2==r1)
print(r.height , r.width)
print(str(r))