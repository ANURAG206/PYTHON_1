#1. Write a program to print the following number patterns using a loop.
#a)
#1
#1 2
#1 2 3
#1 2 3 4
#1 2 3 4 5
#b)
#5 4 3 2 1
#4 3 2 1
#3 2 1
#2 1
#1


a=""
for i in range (1,6):
   a+=str(i) + " "
   print(a)


b="5 4 3 2 1"
for i in range(0,5):
    print(b[i*2::])
