#user input three sides
#check triangel possible or not
a=int(input("side1"))
b=int(input("side2"))
c=int(input("side3"))
if a<b+c and b<a+c and c<a+b:
    print("triangel is possible")
else:
    print("triangel not  possible")