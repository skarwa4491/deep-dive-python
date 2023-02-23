"""
    _summary_
    we can document a function using doc strings.
    if first line in a function body is a string
    not to a varible, not a comment, it is termed as doc string.
    every function has __doc__ property , where doc strings are stored.
    annotations are stoerd in __annotations__ which is a dictionary
"""

def describe_doc_string(a):
    """_summary_
        this is a doc_string , which is compiled in a code,
        which also can be multiline
    """
    return a

def doc_string(a: 'a-string',b :  'a-string')-> 'return a string':
    return a*b

def my_func(a:'int' = 10,b:'int'=1) ->'int':
    """_summary_

    Args:
        a (info on a, optional): number1. Defaults to 10.
        b (info on b, optional): number2. Defaults to 1.

    Returns:
        returns multiplication of two numbers
    """
    return a*b


print(describe_doc_string.__doc__) # this prints a doc string to a function
help(describe_doc_string) # this will print a doc string of a function
print(doc_string(10,20))
print(my_func.__annotations__) # this will print annotations in for of a dict