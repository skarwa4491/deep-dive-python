'''
    should not use mutable objects as default values as default values , 
    unless they are needed
    
    here mutable 2 has default value as a empty list , which stays in memory 
    and returns same list at every execution
    
    
'''

numbers =[]
def mutable(n, numbers):
    numbers.append(n)

def mutable2(n , numbers=[]): # this returns same list everytime to solve this 
    numbers.append(n)
    return numbers

def solve_mutation(n , numbers =[]):
    if not numbers:
        numbers =[]
    numbers.add(n)
    return numbers

nos= mutable2(5)
nos2 = mutable2(6)
print(nos)
print(nos2)
print(nos is nos2)