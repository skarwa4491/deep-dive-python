"""_summary_
    
    high order function, are functions which take another function as parameter
    or return a function
    example: sorted
    
    map returns an iterator , that calculates the function applied to each
    element of a iterable
    map function stops at shorter list when multiple lists are passed
    
    filter function takes a function as a parameter and applies that function
    to each element of iterable. and only include element which satisfies the confition
    
    zip function takes multiple iterables, and returns a list of tuples 
    matching the correspoding elements in a single tuple, and will stop at shortest one
"""

l1 = [2, 3, 4]
l2 = [10, 20, 30]
l3 = [20, 30, 40, 50]


def sq(x):
    return x**2


squares = list(map(sq, l1))
print(squares)

addition = list(map(lambda x, y: x+y, l1, l2))
print(addition)

multiplication = list(map(lambda x, y: x*y, l1, l3))
print(multiplication)
print('-----------------------------filter-------------------------------------- \n')

l = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

even = list(filter(lambda x: x % 2 == 0, l))
print(even)

print('-----------------------------zip--------------------------------------\n')

l1 = [1, 2, 3]
l2 = [10, 20, 30, 40]
l3 = ['a', 'b', 'c']
l4 = 'python'

zipped = list(zip(l1, l2, l3))
print(zipped)
zipped = list(zip(l1, l2, l4))
print(zipped)

print('-----------------------------list comprihension-------------------------------------- \n')

squares = list(map(lambda x: x**2, [i for i in range(10)]))
print(squares)

even = list(filter(lambda x: x % 2 == 0, [i for i in range(10)]))
print(even)

l1 = [2, 3, 4]
l2 = [3, 4, 5]

zipped = [x+y for x, y in zip(l1, l2)]
print(zipped)

l = [1, 2, 3, 4]
even = [x for x in l1 if x % 2 == 0]
print(even)

print('-----------------------------combining map and filter-------------------------------------- \n')

l = range(10)

sq_lt_25 = list(filter(lambda y : y<25 ,map(lambda x : x**2 , l)))
print(sq_lt_25)

sq_lt_25 = [x**2 for x in l if x**2 < 25]
print(sq_lt_25)

