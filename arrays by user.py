from array import *
marks = array(("i"),[])
len = int(input("Enter the length of values"))
for i in range(len):
    x=int(input("Enter the Values :"))
    marks.append(x)
print(marks)
print("sorted list elements are :")
print(sorted(marks))
print("discending Sorted values :")
print(sorted(marks,reverse= True))

val = int(input("Values for search :"))
print(marks.index(val))
print("Reverse Value :")
for k in range(len(marks)-1,-1,-1):
    print(marks)