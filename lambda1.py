from functools  import reduce
# def isEven(i):
#     return i%2==0
# list1=[3,2,8,16,11,34,17]
# output1=list(filter(isEven,list1))
# output2=list(filter(lambda i:i>15,list1))
# output3=list(map(lambda i:i**2,list1))

list1=[10,20,30,40,50]
output=list(map(lambda x:x*3,list1))
print(output)