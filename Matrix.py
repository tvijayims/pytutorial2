#from numpy import *
#i=array([
 #       [1,2,3,4],
  #      [5,6,7,8]
   #     ])
#m = matrix(i)
#print(m)

#now usig matrix function
#from numpy import *
#m= matrix('1 2 3 4 ; 5 6 7 8')
#print(m)
#print(diagonal(m))
#print(m.min())
#print(m.max())

#now adding and multiplication two metrices
from numpy import *
m4= matrix('1 2 3 4 ; 5 6 7 8 ; 1 6 7 9 ; 1 2 3 4')
m1= matrix('3 2 4 5 ; 6 8 9 3 ; 2 3 8 1 ; 1 2 3 4')
m2=m4+m1
m3=m4*m1
print(m2)
print(m3)