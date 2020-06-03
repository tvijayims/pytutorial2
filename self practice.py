def count (list):
    even=0
    odd=0
    for k in range(list):
        if k%2==0:
            even+=1
        else:
            odd+=1
    return even, odd
m=int(input("input length"))
for i in range(m):
    list=int(input("enter value :"))
even, odd = count(list)
print("even :{} and odd :{}".format(even,odd))
