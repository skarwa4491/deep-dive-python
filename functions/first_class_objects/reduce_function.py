"""
    reducing functions
    also called accumelator, aggregator, folding funcitons
"""
from functools import reduce

def _reduce(fn , seq):
    result = seq[0]
    for x in seq[1:]:
        result = fn(result,x)
    return result


result = reduce(lambda x,y : x if x>=y else y , [1,3,6,4,3,5,6,8,9])
print(result)

