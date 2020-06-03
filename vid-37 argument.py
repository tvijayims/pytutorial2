#def update(x):
 #   x=8
  #  print(x)
#update(10)


#def update(x):
 #   x=8
  #  print(x)
#a=10
#update(a)

#mmmutable(because string so id will change)
def update(x):
    print(id(x))
    x=8
    print(id(x))
    print("x",x)
a=10
print(id(a))
update(a)
print("a",a)

#mutable(because list so id will same)
def update(list):
    print(id(list))
    list[1]=25
    print(id(list))
    print("x",list)
list=[10,20,30]
print(id(list))
update(list)
print("a",list)