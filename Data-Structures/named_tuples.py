'''
    named tuples :
        1. namedtuples are function from tuples class
        2. this adds a layer of names to positions a tuples
        3. namedtuple function returns  a class 
        4. named tuples are a class factory
        5. namedtuple take parameter as class name , and field names in same order of data of a tuple
        6. field name can be any name , except '_' preceding
'''
from collections import namedtuple
from re import S

# class approach


class Stock:
    def __init__(self, symbol, year, month, day, open, high, low, close) -> None:
        self.symbol = symbol
        self.year = year
        self.month = month
        self.day = day
        self.open = open
        self.high = high
        self.low = low
        self.close = close


# tuple approach
deepak_nitrate = ('DN', '1991', 'April', '4', 'opened', 1700, 900, '950')

Point = namedtuple('Point',  # classname
                   ['x', 'y']  # required fields
                   )  # this returns a class
pt = Point(10, 20)
print(pt)
print(isinstance(pt, tuple))
print(pt.x, pt.y)
# modifying named tuples
pt = Point(100, pt.y)
print(pt)

Stock = namedtuple(
    'Stock', 'symbol, year , month , day , open , high , low , close')
details = ('DN', '1991', 'April', '4', '901', 1700, 900, 950)

*all_of_it, last = details  # extended unpacking

s = Stock(*all_of_it, last)
print(s._asdict())  # returns dictionary form of a named tuple

# this returns a new tuple with updated named tuple
s = s._replace(symbol='updated')
print(s)
print(s._fields)

# extending named tuple from already created named tuple

new_fields = s._fields+('previous_close',)

StockExt = namedtuple('StockExt' , new_fields)

s_ext = StockExt(*details , 1000)
print(s_ext)