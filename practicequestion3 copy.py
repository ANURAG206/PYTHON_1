#a company decided to give bonus of 1000rs to 
#employee if his servuce more than 5 year 
#ask user salary and year of service and print 
#net bonus amoun


currentsalary=float(input("current salary?"))
serviceperiod=float(input("year of service?"))
if serviceperiod > 5:
    print("net salary will be:",(currentsalary+1000))
else:
    print("net salary will be:",currentsalary)
