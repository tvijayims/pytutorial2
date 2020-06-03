import sys
print(sys.getrecursionlimit())
sys.setrecursionlimit(2000)
i=0
def vijay():
    global i
    i+=1
    print("Hello Vijay")
    vijay()
    vijay()
print(sys.getrecursionlimit())