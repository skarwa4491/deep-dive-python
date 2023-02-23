'''
    *args --> is for variable positional arguments
    * in arguments , is end of positional arguments
    **kwargs --> scoop up varibale keyword args, in form of dictionary
'''


def key_word(**kwargs):
    print(kwargs)


def key_word2(*, d, **kwargs):  # * is end of positional args d=1 and kwargs is a dictionary
    print(d, kwargs)


def key_word3(*args, **kwargs):  # args is tuple and kwargs is a dictionary
    print(args, kwargs)


def key_word4(*, **kwargs):
    '''
        this is not allowed atleast one keyword argument should 
        be given before **kwargs
    '''
    pass

def keyword_5(a, b, *, d, **kwargs):
    print(a, b, d, kwargs)


key_word(a=10, b=20)
key_word2(d=1, a=3, b=2)
key_word3(1, 2, 3, a=1, b=2)
