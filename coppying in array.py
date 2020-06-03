#from numpy import*     by using for loop
#marks = array([1,2,3,4,5])
#for i in marks:
 #   marks=i+5
  #  print(marks)

#from numpy import *     another way
#v = array([1,2,3,4,5,6])
#v=v+5
#print(v)

#adding two array
#from numpy import *
#i=array([1,2,3,4,5])
#j=array([6,7,8,9,3])
#a=i+j
#print(a)
#print(sin(a))
#print(cos(a))
#print(log(a))
#print(sqrt(i))
#print(sum(a))
#print(min(a))
#print(max(a))
#print(concatenate([i,j]))

#aliasing
#from numpy import *
#i=array([1,2,3,4,5,6,7])
#j=i
#print(j)
#print(i)
#print(id(i))
#print(id(j))

#shallow
from numpy import *
i=array([1,2,3,4,5,6,7])
#j=i.view()
j=i.copy()
i[1]=9
print(j)
print(i)
print(id(i))
print(id(j))