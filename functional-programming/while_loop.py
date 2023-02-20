i = 0
while i < 5:
    print(i, end="\t")
    i += 1

# replacement of do while loop

i = 5
while True:
    print(i)
    if (i >= 5):
        print("executing break statement here ")
        break

# while else

l1 = [1, 2, 3]  # add a value , if not present
val = 1
i = 0
while (i < len(l1)):
    if (l1[i] == val):
        break
    i+=1
else:  # this will only execute , if while loop terminated without a break statement
    l1.append(val)
    print(l1)
print(l1)