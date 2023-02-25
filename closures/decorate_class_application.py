'''
    monkey patching - > the process of adding attributes to classes
    dynamically is called monkey patching
'''
from fractions import Fraction
# adding a instace method dynamically
# Fraction.speak = lambda self, message: 'Fraction says {}'.format(message)
Fraction.is_integral = lambda self: True if self.denominator == 1 else False

f = Fraction(2, 1)
print(f.is_integral())

def decorate(cls):
    cls.speak = lambda self, message : '{} says {}'.format(self.__class__.__name__,message)
    return cls

Fraction = decorate(Fraction)

f = Fraction(10,20)
print(f.speak('Hello'))