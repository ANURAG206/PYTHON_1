a=int(input("enter input 1 :"))
b=int(input("enter input 2 :"))
o=input("choose operator")
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mult(a,b):
    return a*b
def divide(a,b):
    return a/b
if o=="add":
    print(add(a,b))
elif o=="sub":
    print(sub(a,b))
elif o=="mult":
    print(mult(a,b))
elif o=="divide":
    print(divide(a,b))
else:
    print("invalid")
    