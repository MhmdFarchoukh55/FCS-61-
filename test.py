d={}
liste=[]
action="yes"
while action !="no":
    name=input("enter tour name")
    date=input("enter the date")
    d["name"]=name
    d["date"]=date
    newItem=""
    d2={}
    while newItem!="exit":
        newItem=input("enter the name of the item")
        if newItem !="exit":
            price=float(input("enter the price"))
            d2[newItem]=price
            liste.append(d2)
        else:
            action=input("ffffff")    
print(d)
        

