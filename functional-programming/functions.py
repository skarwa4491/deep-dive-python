'''
    functions are objects in python
    functions are just like variables in python , with name of a function name
    
    'def' keyword creates the function, with given name , variables and function code
'''

def func_1():
    print('execute function 1')

print(func_1) # this will print func_1 as object

func_1() # this will call function

def function_1(a : int , b : int): # this is just for documentation purpose
    pass

def func_3():
    '''
        this will not give error , as python is just creating 
        a function and not executing it 
    '''
    return func_4() 

def func_4():
    print('Hello world')

func_3()

def func_5():
    '''
        this will give error , as we are calling func_6 , before its decleration
    '''
    return func_6() 

func_5()

def func_6():
    print('Hello world')

#-------------------------------- lambda function ----------------------------------------

lambda_function = lambda x : x**2
lambda_function()
