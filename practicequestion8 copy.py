# company will give bonus if
#    time spent in company            bonus
#    greater than 10                10%
#    more than 6 and less than 10    8%
#    less than 6                     5%


currentSalary=int(input("your currnt salart:"))
servicePeriod=int(input("time spent:"))
if servicePeriod>10:
    print("net salary:",((currentSalary)*0.1+currentSalary))
elif servicePeriod>6 and servicePeriod<10:
    print("net salary:",((currentSalary)*0.08+currentSalary))
elif servicePeriod<6:
    print("net salary:",((currentSalary)*0.05+currentSalary))
else:
    print("net salary=currentSalary")