#take input of age of 3 people
#determine oldest and youngenst


age1=int(input("age of 1st person:"))
age2=int(input("age of 2nd person:"))
age3=int(input("age of 3rd person:"))
if age1  >age2  and age1>age3:
    print("1st is oldest")
elif age2>age1 and age2>age3:
    print("2nd persn is oldest")
elif age3>age1 and age3>age2:
    print("3rd is oldest")
else:
    print("all are of same age")

