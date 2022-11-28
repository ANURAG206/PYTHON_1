#Using a for loop and .append() method append each item with a Dr. prefix
#to the lst.
#list1=["Phil", "Oz", "Seuss", "Dre"]
def a(val):
    if(val==0 or val==1):return 1
    else:return val*a(val-1)
num=int(input("enter no.:"))
print("factorial= ",a(num))