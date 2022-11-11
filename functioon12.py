#create a function that will display the how many items in the list have names more than 5 characters 
def charaters(name):
    more=0
    less=0
    for i in name:
        if len(i)>5:
            print(i)
            more+=1
        else:
            less+=1
    return more,less
name=["subham","anurag","atul"]
more,less=charaters(name)
print(more)
print(less)

