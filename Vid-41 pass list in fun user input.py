from array import *
def count (m):
    even=0
    odd=0
    for k in range(m):
        if k%2==0:
            even+=1
        else:
            odd+=1
    return even, odd
numbers= array("i",[])
len=int(input("Enter the length of numbers :"))
for j in range(len):
    m=int(input("Enter the values :"))
    numbers.append(m)
even, odd = count(m)
print("even :{} and odd :{}".format(even,odd))
