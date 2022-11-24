#. Display Fibonacci series up to 10 terms
#The Fibonacci Sequence is a series of numbers. The next number is found
#by adding up the two numbers before it. The first two numbers are 0 and 1.
def a(val):
    if(val==1):return 0
    elif(val==2):return 1
    else:return a(val-1)+a(val-2)
for i in range(1,11):print(a(i),end=" ")