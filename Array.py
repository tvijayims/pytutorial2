from array import *
num = array('i',[5,6,8,9,10])
newArr = array(num.typecode,(a*a for a in num))
for e in newArr :
    print(e)
print(sorted(newArr))
print("reverse number :")
for i in range(len(newArr)-1,-1,-1):
    print(newArr[i]),