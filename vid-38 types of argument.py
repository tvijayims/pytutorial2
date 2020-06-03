def add(x,y):
    z=x+y
    print(z)

add(5,6)
#positions
def person(name,a,age):
    print(name)
    for i in range (a):
        age+=5
        print(age)
person("vijay",1,25)
#keyword
def person(name,a,age):
    print(name)
    for i in range (a):
        age+=5
        print(age)
person(a=1,age=28,name="navin")

#default
def person(name,age=18):
    print(name)
    print(age)
person(name="navin")

#varriable lenghth
def sum(a,*b):
    c=a
    print(b)
    for i in b:
        c=c+i
    print(c)
sum(5,6,8,9)