#ex1
age=input("Enter your age: ")
if age<=8:
    print("The ticket price is $5.")
else:
    print("The ticket price is $15.")


#ex2
number=int(input("Enter a number: "))
if number%2==0:
    print("The number",number,"is even.")
else:
    print("The number",number, "is odd.")

#ex3
#If the username is "admin" and the password is "1234", print "Access granted".
username=input("enter username")
password=input("enter ur password")
if username=="admin":
    if password=="1234":
        print("Access granted")
    else:
        print("Access denied")
else:
    print("Access denied")
#2emethode
if username=="admin" and password=="1234":
    print("Access granted")
else:
    print("Access denied")