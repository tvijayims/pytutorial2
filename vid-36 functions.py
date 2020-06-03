from numpy import *
def vijay():
    print("Kumar")
    print("thakur")

vijay()

def add(x,y):
    z=x+y
    #print(z)
    return z

result=add(5,6)
print(result)

def add_sub(x,y):
    z=x+y
    n=x-y
    #print(z)
    return z,n

result,sub=add_sub(11,6)
print(result,sub)