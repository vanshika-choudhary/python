# Write a program to check if a number is positive.

num1=int(input("enter a number:"))
if num1>=0:
    print("number is positive")
else:
    print("number is negative")

# Write a program to check whether a number is even or odd.

num2=int(input("enter a number:"))
if num2%2==0:
    print("number is even")
else:
    print("number is odd")

# Write a program to assign grades based on marks:
# A for 90 and above
# B for 75–89
# C for 50–74
# Fail for below 50

marks=int(input("enter your marks:"))
if marks>=90:
    print("you have A grade") 
elif marks<=75 and marks>=89:
    print("you have B grade")
elif marks<=74 and marks>=50:
    print("you have C grade")
else:
    print("you are fail") 

# Write a program to check whether a person is eligible to vote or not.

age=int(input("enter your age:"))
nationality=input("enter your nationality as indian or other")
if age>18 and nationality=="indian" :
    print("you are eligible")
else:
    print("you are not eligible")

# Write a program to check whether a student has passed and determine the division:
# First Division: Marks ≥ 60
# Second Division: Marks ≥ 45 and < 60
# Third Division: Marks ≥ 40 and < 45
# Fail: Marks < 40

marks=int(input("enter your marks:"))
if marks>=60:
    print("you got first division")
elif marks >= 45 and marks< 60:
    print("you got second grade")
elif marks>=40 and marks<45:
    print("you got third division")
else:
    print("you are fail")        
# Write a program to display the month name based on the month number entered (1–12).

num=int(input("enter your month number:"))
if num==1:
    print("your month name is january")
elif num==2:
    print("your month name is february")
elif num==3:
    print("your month name is march")
elif num==4:
    print("your month name is april")
elif num==5:
    print("your month name is may")
elif num==6:
    print("your month name is june")
elif num==7:
    print("your month name is july")
elif num==8:
    print("your month name is august")
elif num==9:
    print("your month name is september")
elif num==10:
    print("your month name is october")
elif num==11:
    print("your month name is november")
else:
    print("your month name is december")

# Write a program to check if a student's attendance is 75% or above. If yes, display "Eligible for Exam".

att=int(input("enter your attendance"))
if att>74:
    print("eligible foir exam")
else:
    print("not eligible for exam")

# Write a program to calculate electricity bill category:
# Below 100 units → Low Usage
# 100–300 units → Medium Usage
# Above 300 units → High Usage

bill=int(input("enter your units usage"))
if bill>300:
    print("high usage")
if bill<=300 and bill>=100:
    print("medium usage")
else:
    print("low usage")
