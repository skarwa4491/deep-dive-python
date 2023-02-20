class Rectangle:
    
    def __init__(self , width , height):
        self.height = height
        self.width = width
    
    def area(self):
        return self.width*self.height

    def perimeter(self):
        return 2*self.width+ 2*self.height
    
    def __str__(self) -> str: # this overrides str method
        return 'reactange width = {width} , height ={height}'.format(width=self.width , height = self.height)
    
    def __repr__(self) -> str:
        return 'Reactagle({0} , {1})'.format(self.width , self.height)
    
    def __eq__(self , other) -> str:
        if isinstance(other,Rectangle):
            return (self.width == other.width and self.height == other.height)
        else:
            return False
    
r = Rectangle(10, 20)
rr = Rectangle(10 , 20)
print(r.height , r.width)
print(r.area() , r.perimeter())
print(str(r) , hex(id(r)) )
print(r == rr)