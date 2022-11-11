#make calculator
num1=float(input("enter"))
num2=float(input("enter"))
a=input("enter operator")
if a=="+":
    print(num1+num2)
elif a=="-":
    print(num1-num2)
elif a=="*":
    print(num1*num2)
elif a=="/":
    print(num1/num2)
else:
    print("invalid")