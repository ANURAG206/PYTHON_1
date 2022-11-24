#Write a program to display all prime numbers within a range
#Take the user input for start and end of range.
a=int(input("first"))
b=int(input("second"))
for i in range(a,b+1):
    if i>1:
        for j in range(2,i):
            if(i%j==0):break
        else:
            print(i,end=" ")
