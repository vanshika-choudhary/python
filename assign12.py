# Q1. Create and Write to a File
# Write a Python program to create a file named student.txt and store the following information:
# Name
# Course
# City

name=input("enter the student name:")
course=input("enter the course name:")
city=input("enter the city name:")
with open("student.txt","w") as f:
    f.write(f"name:{name}\ncourse:{course}\ncity:{city}")

# Q2. Read File Contents
# Write a Python program to read and display all the contents of the file student.txt.

with open("student.txt","r") as f:
    print(f.read())

# Q3. Append Data to a File
# Write a Python program to append a new line containing a phone number to student.txt and then display the 
# updated contents of the file.

with open("student.txt","a") as f:
    f.write("\nphone no:780xxxxxx7")
with open("student.txt","r") as f:
    print(f.read())

# Q4. Calculator Using Exception Handling
# Create a menu-driven calculator that performs:
# Addition
# Subtraction
# Multiplication
# Division
# Handle all possible exceptions such as:
# Invalid input
# Division by zero
# Wrong menu choice

try:
    a=int(input("enter the first number:"))
    b=int(input("enter the second number:"))
    choice=input("enter '+' for addition,'-' for subtraction '*' for multipication '/' for division:")
    if choice=="+":
        print(a+b)
    elif choice=="-":
        print(a-b)
    elif choice=="*":
        print(a*b)
    elif choice=="/":
        print(a/b)
    else:
        print("invalid choice!!")
except Exception as e:
    print(e)

# Q5. Write a Python program that asks the user to enter a filename and reads the file. Handle the
#  FileNotFoundError exception if the file does not exist.

file_name=input("enter the file name:")
try:
    with open(file_name,"r") as f:
        f.read()
except FileNotFoundError:
    print("your file not found")

# Q6. Write a Python program that accepts two numbers from the user and performs division. Handle exceptions such as:
# Division by zero
# Invalid input

try:
    a=int(input("enter the first number:"))
    b=int(input("enter the second number:"))
    print(a/b)
except Exception as e:
    print(e)

# Q7.  Write a Python program that accepts the user's age and validates it using exception handling.
# Conditions:
# Age should be between 1 and 120.
# Raise an exception for invalid ages.

try:
    age=int(input("enter the age:")) 
    if age<1 or age>120:
        raise ValueError("age must be between 1 to 120")
    print("valid age:",age)
except ValueError as e:
    print("invalid age",e)

# Q8. Write a Python program to read a file and handle exceptions that may occur during file operations.

try:
    file=input("enter the file name:")
    with open(file,"r")as f:
        f.read()
except Exception as e:
    print(e)

# Q9. Create a list containing five elements. Ask the user to enter an index and display the corresponding element.
#  Handle the IndexError exception if the index is out of range.

l=[34,67,56,98,74]
idx=int(input("enter the index:"))
try:
    l[idx]
except IndexError as e:
    print(e)

# Q10. Create a dictionary containing student information. Ask the user to enter a key and display the corresponding 
# value. Handle the KeyError exception if the key does not exist

d={"name":"vanshika", "class":"btech cse"}
key=input("enter the key name you want to access:")
try:
    print(d[key])
except KeyError as e:
    print("this key doesnot exist",e)