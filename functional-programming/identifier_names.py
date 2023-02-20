# identifier names are case sensitive 
var = 10
Var = 10

# both above are different
# identifiers must follow certain rules and conventions 
'''
    Rules 
        1. must start with '_' or letter (a-z) or  (A-Z) or (0-9)
        2. cannot be reserved words
        3. package names , should be short , preferrable no underscore
        4. for modules , can have underscore
        5. for classes , use camel case
        6. functions , lower case , and seperation should be '_'
        7. variables, same as functions
        8. constants, all uppercase and seperated by '_' 
'''

'''
    Explanation:
        1. starts with single '_' it is internal , or private oibject
        Objects named this way will not be imported by *
        2. starts with '__' is used for name mangling 
        3. starts and ends with '__' , these are system defined names , and suggest not to create 
        our own , while use what python gives
        ex :
            x < y ------> x.__lt__(y)
            
        
'''