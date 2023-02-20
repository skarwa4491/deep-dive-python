'''
    Python iterable are objects , which are capable of returning 
    object one at a time ex : list, set , tuple etc
    
    for loop allows us to iterate over iterable
    
    range function creates an iterable 
'''
for i in range(4): # uses iterable object
    print(i , end = "\t")


print()
l = [1,2,3,4]

for i in l:
    print(i , end= '\t')
    
s = "abcd"
print()
for ch in s:
    print(ch , end = "\t")

lot = [(1,2) , (3,4) ,(5,6)]

print()
for x in lot:
    print(x , end = "\t") # this will print each tuple
print()

for i , j in lot: # this will unpack tuple and assign to values to i ,j 
    print(i , j , end="\t")
print()

for i in range(1,5):
    print(i , end = "\t")
    if i%7 == 0:
        break
else:
    print()
    print("this executed because , break was not executed")

s = "hello"
for i , c in enumerate(s):
    print(i,c , end="\t")