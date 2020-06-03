def fact(x):
    f=1
    for i in range(1,x+1):
        f=f*i
    return f
x=int(int(input("Enter fact number :")))
result=fact(x)
print(result)