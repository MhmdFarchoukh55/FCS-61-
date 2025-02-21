def TotalAmount(dic1,month):
    sum=0
    for i in dic1[month]["expensive"].values():
        sum+=i
    return sum

def AmountAllocated(dic2,month):
    x=dic2[month]["salary"]
    y=dic2[month]["expensive"]["Savings"]*x/100
    w=dic2[month]["expensive"]["Electrecity"]*x/100
    t=dic2[month]["expensive"]["Rent"]*x/100
    return y+w+t

def remainder(dic,mo):
    Salary=dic[mo]["salary"]-AmountAllocated(dic,mo)
    return Salary

def monthPay(dic):
    sum=0
    for i in dic:
        sum+=dic[i]["salary"]        
    return sum
salary=0
month=""
percentageSavings=0
percentageRent = 0
percentageElectricity =0
BigDict={}
SmallDict={}
expensive={}
while month!="finish": 
    month=input("enter the month ")
    if month !="finish":
        salary=float(input(f"enter the salary for the month {month} "))
        percentageSavings=float(input(f"enter the Saving for the month {month} ")) 
        percentageRent =float(input(f"enter the Rent for the month {month} ")) 
        percentageElectricity =float(input(f"enter the Electrecity for the month {month} "))
        SmallDict["salary"]=salary
        expensive["Savings"]=percentageSavings
        expensive["Rent"]=percentageRent
        expensive["Electrecity"]=percentageElectricity
        SmallDict["expensive"]=expensive
        BigDict[month]=SmallDict
ask1=input("Do you want to know The total amount spends on savings,rent,and electricity combined.")
if ask1=="yes":
    ask11=input("enter the month ")
    print(BigDict) 
    print(f'total expensive {AmountAllocated(BigDict,ask11)}')
    print(f'Remaining salary:  {remainder(BigDict,ask11)}')
    print(f'the total salary of the year {monthPay(BigDict)}')
