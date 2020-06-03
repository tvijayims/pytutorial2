from array import *
num = array('i',[5,6,8,9,10])
newArr = array(num.typecode,(a*a for a in num))
i=0
while i<len(newArr):
    print(newArr[i])
    i+=1