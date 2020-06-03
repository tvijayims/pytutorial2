a=10
def vijay():
    global a
    a = 15
    print("in Function",a)
vijay()
print("outside",a)


#global and local
a=10
print(id(a))
def vijay():
    a = 15
    b=globals()['a']
    print(id(b))
    globals()['a']=118
    print(id(a))
    print("in Function",a)
vijay()
print("outside",a)