from functools import reduce
def is_even(n):
    return n%2==0
def update(n):
    return n+2
def add_all(a,b):
    return a+b

num=[3,4,5,6,7,8,9,1,2]
evens =list(filter(is_even,num))
plustwo=list(map(update,evens))
addall=reduce(add_all,plustwo)
print(evens)
print(plustwo)
print(addall)





##now lamda
num=[3,4,5,6,7,8,9,1,2]
evens =list(filter(lambda n:n%2==0,num))
plustwo=list(map(lambda n:n+2,evens))
addall=reduce(lambda a,b:a+b,plustwo)
print(evens)
print(plustwo)
print(addall)