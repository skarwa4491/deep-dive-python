"""
    1. packed values are refered to iterables
    2. Tuples are created by , and not ()
        ex: 1,2,3 is a tuple
            1, is a tuple
            () or tuple() is empty tuple
    3. unpacking is process of splitting all elements into an indivisual variables 
"""

a, b, c = [1, 2, 3]  # a=1 , b=2 , c=1
a, b, c = [1, 2, 'hello']  # a= 1 , b=2 , c='hello'
(a, b, c) = 'XYZ'  # a=X,b=Y,c=Z

# swapping of variables

a, b = 10, 20
print('before swapping a={} , b={}'.format(a, b))
a, b = b, a
print('after swapping a={} , b={}'.format(a, b))

# unpacking sets and dictionaries

d = {'key1': 'val1', 'key2': 'val2'}  # dict and sets are unordered types
#####################################################################################################

# to use * , use python 3.5 or greater

# this is slicing
l = [1, 2, 3, 4, 5, 6]
a = l[0]
b = l[1:]
print(a, b)

# this is new syntax
a, *b = l  # a = first element , and rest everything in b
print(a, b)

a, *b = 'XYZ'
print(a, b)

a, b, *c, d = l
print(a, b, c, d)

# * oeprator can only be used once in LHS
###################################################################
# * on RHS

l1 = [1, 2, 3]
l2 = [3, 4, 5]
l = [*l1, *l2]
print(l)

d1 = {'p': 2, 'y': 1}
d2 = {'t': 3, 'h': 2}

d = {*d1, *d2}
print(d)  # this will unpack only keys of d1 and d2

# this will unpack dictionary , and ** operator can only be used on RHS
d = {**d1, **d2}

d1 = {'a': 1, 'b': 2}
d = {'a': 10, 'c': 3, **d1}  # this will override value of a

print(d)
#####################################################################

a, b, (c, d) = [1, 2, [3, 4]]  # unpacking nested
print(a, b, c, d)

a, *b, (c, d, e) = [1, [2, 3], 'XYZ']  # nested unpacking
print(a, b, c, d, e)

a, *b, (c, *d) = [1, 2, 3, 'hello'] # this is okay because * is used in a different expression
print(a, b, c, d)
