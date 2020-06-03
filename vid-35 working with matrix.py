#from numpy import *
#i=array([
 #       [1,2,3,4],
 #       [5,6,7,8]
#      ])
#print(i)
#print(i.dtype)
#print(i.ndim)
#print(i.shape)
#print(i.size)

#2D into 1D
from numpy import *
i=array([
        [1,2,3,4,9,10],
        [5,6,7,8,11,12]
        ])
j=i.flatten()
print(j)
#1D to 3D
#a=j.reshape(3,4)
a=j.reshape(2,2,3)
print(a)