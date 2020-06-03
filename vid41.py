def count (list):
    even=0
    odd=0
    for k in (list):
        if k%2==0:
            even+=1
        else:
            odd+=1
    return even, odd
list=[1,2,3,4,5,6,7,8,9]
even, odd = count(list)
print("even :{} and odd :{}".format(even,odd))
