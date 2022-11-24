colors=["RED","BLUE","BLACK",22]
cars=["tata","nanao","jeep","alto"]
#colors[1:3]="pink","baby"
#colors.insert(2,"indigo")
#colors.append("car")
#colors.extend(cars)
#colors.pop(1)
# print(colors)
#pop rremove specific index
#del remove entire list
#x=0
#while x<len(cars):
 #    print(cars[x])
  #  x+=1
#[print(x) for x in cars]
newlist=[]
for i in cars:
    if "a" in i:
        newlist.append(i)
print(newlist)