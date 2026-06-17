# Print numbers from 1 to 10 using recursion.

def print_no(n=1):
    if n==11:
        return
    print(n)
    print_no(n+1)
print_no()
print("------------------------------------------")

# Print numbers from 10 to 1 using recursion.

def print_no(n=10):
    if n==0:
        return
    print(n)
    print_no(n-1)
print_no()
print("------------------------------------------")

# Find the sum of first N natural numbers using recursion.

sum=0
def sum_no(n):
    if n==1:
        return 1
    global sum
    return n+sum_no(n-1)
no=int(input("enter the no upto which u want sum of natural no:"))
print("sum of",no,"natural no is",sum_no(no))
print("------------------------------------------")

# Find the factorial of a number using recursion.

def fact(n):
    if n==1:
        return 1
    return n*fact(n-1)
no=int(input("enter the no whose factorial you want:"))
print("factorial of",no,"is",fact(no))
print("------------------------------------------")

# Find the power of a number using recursion.

def pow(n,num):
    if n==1:
        return num
    return num*pow(n-1,num)
num=int(input("enter the number:"))
n=int(input("enter the power raised to that number:"))
print("so",num,"raised to power",n,"is",pow(n,num))
print("-------------------------------")

# Find the sum of digits of a number using recursion.

def sum(n):
    if n<10:
        return n 
    return (n%10)+sum(n//10)
print(sum(568))    
print("---------------------------------")

# Count the number of digits in a number using recursion.

def count(n):
    if n<10:
        return 1
    return 1+count(n//10)
num2=int(input("enter the number:"))
print("this number has",count(num2),"digits")
print("-------------------------------")

# Reverse a number using recursion.

def reverse(n):
    if n<10:
        print (n,end="")
    else:
        print(n%10,end="")
        reverse(n//10)
numb=int(input("enter your number"))
reverse(numb)

# Create a lambda function to find the square of a number.

s=lambda a:a**2
num=int(input("enter the number:"))
print(s(num))
print("--------------------")

# Create a lambda function to find the cube of a number.

cube=lambda n:n**3
num3=int(input("enter the number:"))
print(f"cube of {num3} is {cube(num3)}")
print("------------------")

# Create a lambda function to find the sum of two numbers.

l2=lambda a,b:a+b
num4=int(input("enter the first number:"))
num5=int(input("enter the second number:"))
print(f"the sum of {num4} and {num5} is {l2(num4,num5)}")
print("--------------------------------")

# Create a lambda function to find the product of two numbers.

l3=lambda a,b:a*b 
num6=int(input("enter the first number:"))
num7=int(input("enter the second number:"))
print(f"the sum of {num6} and {num7} is {l3(num6,num7)}")
print("--------------------------------")

# Create a lambda function to check whether a number is even or odd.

l4=lambda a:"Even no" if num8%2==0 else "odd no"
num8=int(input("enter the no:"))
print(l4(num8))
print("-------------------------------------")

# Create a lambda function to check whether a number is positive, negative, or zero.

l5=lambda x:"positivie number" if x>0 else "zero" if x==0 else "negative number"
num9=int(input("enter the no:"))
print(l5(num9))
print("-------------------------------------")

# Create a lambda function to find the greater of two numbers.

l6=lambda a,b:"first no is the greatest" if a>b else "both numbers are the same" if a==b else "second number is greater"
num10=int(input("enter the first number"))
num11=int(input("enter the second number"))
print(l6(num10,num11))
print("----------------------------------")

# Create a lambda function to find the smallest of three numbers.

l7=lambda a,b,c:f"{a} is the greatest number"if a>b and a>c else f"{b} is the greatest number" if b>a and b>c else f"{c} is the greatest number"
num12=int(input("enter the first number:"))
num13=int(input("enter the second number:"))
num14=int(input("enter the third number:"))
print(l7(num12,num13,num14))
print("----------------------------------")