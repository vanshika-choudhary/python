# Type Conversion Practice Questions
# 1. Basic Conversion:
# ○ Write a program that converts an integer to a float and a float to an integer.
# Input: 5 (as integer)
# Output: 5.0 (as float), 5 (back to integer)

num=int(input("enter the number"))
num1=float(num)
num2=int(num1)
print(num1,"(as float),",num2,"(back to integer)")

# 2. String to Number:
# ○ Write a program that takes a string input of a number (e.g., &quot;45&quot;) and converts it into an
# integer. Then, print the square of that number.

num=input("enter the string of number")
num=int(num)
print(num**2)

# 3. Mix and Match:
# ○ Convert the following:
# ■ &quot;3.14&quot; to a float
# ■ 98 to a string
# ■ True to an integer
# ■ &quot;Hello&quot; to a boolean

num1=3.14
num2=98
num2=str(num2)
num3=int(True)
num4=bool("hello")

# 4. TypeError Practice:
# ○ Write a program to handle this case:
# Input: &quot;3.5&quot;
# Task: Convert it to an integer and handle any errors gracefully.

num5=int(3.5)

# Input Function Practice Questions
# 1. Basic Input:
# ○ Write a program that takes the user’s name and age as input and prints a greeting like:
# &quot;Hello John! You are 25 years old.&quot;

name=input("enter you name")
age=input("enter your age")
print("hello",name,"! you are",age,"years old")

# 2. Sum of Numbers:
# ○ Write a program that asks the user to input two numbers and prints their sum.

no1=int(input("enter first no."))
no2=int(input("enter second no."))
print(no1+no2)

# 3. Type-Casting in Input:
# ○ Write a program to take two numbers as input (both in string format), convert them to
# integers, and print their product.


# 4. Custom Conversion:
# ○ Write a program that asks the user for a temperature in Celsius, converts it to Fahrenheit,
# and prints the result.
# Formula: F = (C × 9/5) + 32

# Operators Practice Questions
# 1. Arithmetic Operators:
# ○ Write a program that takes two numbers as input and performs all arithmetic operations
# (addition, subtraction, multiplication, division, modulus, floor division, and exponentiation)
# on them. Print the results.
# 2. Comparison Operators:

# ○ Write a program that asks for two numbers and compares them using all comparison
# operators (==, !=, &lt;, &gt;, &lt;=, &gt;=). Print True or False for each comparison.

# 3. Logical Operators:
# ○ Write a program that takes three boolean inputs (e.g., True, False) and evaluates the
# following expressions:
# ■ (a and b)
# ■ (a or b)
# ■ not a

# 4. Compound Assignment Operators:
# ○ Write a program that initializes a number to 10 and uses the +=, -=, *=, and /= operators to
# modify the number.

# 5. Odd or Even:
# ○ Write a program that takes a number as input and uses the modulus operator % to
# determine if it is odd or even.