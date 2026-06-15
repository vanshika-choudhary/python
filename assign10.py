# Question 1: Secure Login System
# Create a login system using while True.
# Requirements:
# Correct Username: admin
# Correct Password: Python@123
# Rules:
# User gets only 3 attempts.
# If username or password is incorrect:
# Invalid Credentials
# After 3 failed attempts:
# Account Locked
# and stop the program.
# If login is successful:
# Welcome Admin
# and stop the loop.

print("Program 1:secure login system")
attempt=0
while True:
    username=input("enter your username:")
    passw=input("Enter your password:")
    if username=="admin" and passw=="Python@123":
        print("Login succesfull!!!")
        print("Welcome Admin")
        break
    else:
        print("Invalid credentials")
        attempt+=1
        if attempt==3:
            print("you have tried 3 failed attempts!!\n Now your account is locked")
            break
        else:
            continue
print("------------------------------------")


# Question 2: Product Inventory System
# Create a menu-driven program using while True.
# Menu:
# 1. Add Product
# 2. View Products
# 3. Search Product
# 4. Exit
# Requirements:
# Store products in a list.
# Add new products.
# Display all products.
# Search a product by name.
# Exit the program when user selects option 4.
# Use functions wherever possible.

print("Program 2:product inventory system")

print("1.-- to add product")
print("2.-- to view product")
print("3.-- to search product")
print("4.-- to exit")
l=[]
def add():
    pr=input("enter the product you want to add:")
    l.append(pr)
    print("product added succesfully!!!")
def view():
    print(l)
def search():
    pr=input("Enter the product name to search in list:")
    if pr in l:
        print("product is in the list at index :",l.index(pr))
    else:
        print("sorry :[  product not found in list!!")
while True:
    choice=input("Enter your choice:")
    if choice=="1":
        add()
    elif choice=="2":
        view()
    elif choice=="3":
        search()
    elif choice=="4":
        break
    else:
        print("Invalid choice... please type again")
print("-------------------------")    

# Question 3: Mini Banking System 
# Create a banking system using functions and while True.
# Initial Balance:
# 10000
# Menu:
# 1. Check Balance
# 2. Deposit Money
# 3. Withdraw Money
# 4. Transaction History
# 5. Exit
# Requirements:
# Deposit updates balance.
# Withdrawal should not exceed available balance.
# Store every transaction in a list.
# Show all transactions when user selects Transaction History.
# Use separate functions for deposit, withdraw, and balance check.
# Example Transaction History:
# Deposited ₹5000
# Withdrawn ₹2000
# Deposited ₹1000

print("Program 3")

print("1---to check bank balance")
print("2---to deposit money")
print("3--to withdraw cash")
print("4--to see transaction history")
print("5--to exit program")
balance=10000
his=[]
his.append(["current balance",balance])
def b_balance():
    global balance
    print("your current bank balance is",balance)
def deposit():
    amount=int(input("enter the amount you need to deposit:"))
    global balance
    balance+=amount
    his.append(["deposit",amount])
    print("your amount of",amount,"is succesfully deposited")
def withdraw():
    amount=int(input("enter the amount you need to withdraw:"))
    global balance
    if amount<=balance:
        balance-=amount
        print("your",amount,"is debited from your account")
        his.append(["withdrawal",amount])
    else:
        print("you dont have enough money to withdraw!!\n try again with a smaller amount")
def transac():
    print("ypur transaction history is:")
    print(his)
while True:
    choice=input("enter your choice:")
    if choice=="1":
        b_balance()
    elif choice=="2":
        deposit()
    elif choice=="3":
        withdraw()
    elif choice=="4":
        transac()
    elif choice=="5":
        print("program stops here!!")
        break
    else:
        print("Invalid choice please enter again")
print("--------------------------")

# Question 4: Student Management System
# Create a menu-driven program using functions and while True.
# Menu:
# Add Student
# View Students
# Search Student
# Delete Student
# Exit
# Requirements:
# Store student records in a dictionary.
# Roll Number as key.
# Student Name as value.
# Search student by roll number.
# Delete student record.
# Use functions for each operation.
# Example:
# Enter Roll No: 101
# Enter Name: abc
# Student Added Successfully

print("Program 4")

print("1---to add student")
print("2---to view student")
print("3--to search student")
print("4--to delete student")
print("5--to exit program")
d={}
def add():
    roll=int(input("enter student's rollno:"))
    name=input("enter student name:")
    d.update({roll:name})
    print("Student record added succesfully!!!")
def view():
    for keys,value in d.items():
        print("student rollno:",keys,"student name",value)
def search():
    roll=int(input("Enter the rollno of student you want to search:"))
    if roll in d.keys():
        print("student record with rollno",roll,"is present in record!!")
    else:
        print("student record with rollno",roll,"not found!!!")
def delete():
    roll=int(input("enter the rollno of student who you want to delete:"))
    d.pop(roll)
    print("student record removed succesfully!!!")
while True:
    choice=input("enter your choice:")
    if choice=="1":
        add()
    elif choice=="2":
        view()
    elif choice=="3":
        search()
    elif choice=="4":
        delete()
    elif choice=="5":
        print("program stopped!!!")
        break
    else:
        print("Invalid choice please enter again")
print("-----------------------------------------------")

# Question 5:
# 1
# 23
# 456
# 78910
no=1
for i in range(1,5):
    for j in range(0,i):
        print(no,end="")
        no+=1
    print()
print("----------------------------")
# 54321
# 5432
# 543
# 54
# 5

for i in range(5):
    for j in range(5,i,-1):
        print(j,end="")
    print()
print("------------------")

# 5
# 45
# 345
# 2345
# 12345

for i in range(5,0,-1):
    for j in range(i,6):
        print(j,end="")
    print()