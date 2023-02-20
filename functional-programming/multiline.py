# not legal
if a
    and b
    and c
    
# legal

if a \ # cannot put comments after \
    and b\
    and c: # can be commented here
        
#__________________________________________________________________________________________________
 #multiple line string 
 
    """
        this is a multiple 
        line string 
    """
    or 
    '''
        this is a multiple 
        line string 
    '''
#__________________________________________________________________________________________________
# multiline list
# valid list
a = [1,
        2
        3]
b = [1,2
     3,4,5]

c = [1, # comments allowed
     2]