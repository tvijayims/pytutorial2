x=int(input("Enter number : "))
for i in range(2,x):
    if x%i==0:
        print("Not Prime")
        break
else:
    print("Prime")