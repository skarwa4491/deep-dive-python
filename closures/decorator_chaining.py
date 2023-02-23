def dec1(fn):
    def inner():
        print('decorator - 1')
        return fn()
    return inner

def dec2(fn):
    def inner():
        print('decorator - 2')
        return fn()
    return inner

@dec1
@dec2
def func():
    print('function')

func()