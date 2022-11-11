#take input if lenght of input more than 3 add ing  to last otherwise same
wrd=input("enter name")
l=len(wrd)
if l>3:
    print(wrd+"ing")
else:
    print(wrd)