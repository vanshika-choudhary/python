# Check if a person is eligible to vote. If eligible, check whether they have a voter ID card.

age=int(input("enter your age:"))
id=input("you have voter id card? yes or no:")
if age>18 and id=="yes":
    print("you are eligible to vote")
else:
    print("you are not eligible to vote")

# Check if a person is 18 years or older. If yes, check whether they have a driving license.

age=int(input("enter your age:"))
license=input("you have driving license? yes or no:")
if age>18 and license=="yes":
    print("you are eligible to drive")
else:
    print("you are not eligible to drive")

# Print numbers from 1 to 10 using a for loop.

for i in range(1,11):
   print(i)

# Print numbers from 10 to 1 in reverse order.

for i in range(10,0,-1):
    print(i)

# Print all even numbers between 1 and 50.

for i in range(2,51,2):
    print(i)

# Print all odd numbers between 1 and 50.

for i in range(1,50,2):
    print(i)

# Print the multiplication table of a given number.

num=int(input("enter the number whose table u want to print:"))
for i in range(11):
    print(num,"X",i,"=",num*i)

# Print the cube of numbers from 1 to 10.

for i in range(1,11):
    print(i**3)

# Find the sum of numbers from 1 to 10.

sum=0
for i in range(11):
    sum+=i 
print("the sum from 1 to 10 is",sum)

# Find the sum of numbers from 1 to N.

num2=int(input("enter the value upto which u need the sum:"))
sum2=0
for i in range(num2+1):
    sum2+=i
print(sum2)

# Print the multiplication table of 2.

for i in range(11):
    print("2 X",i,"=",2*i)

# Print the multiplication table of a given number.

num3=int(input("enter the number whose table u want to print"))
for i in range(11):
    print(num3,"X",i,"=",num3*i)

# Count how many numbers are there from 1 to 100.

count=0
for i in range(100):
    count+=1
print("numbers between 1 to 100 are",count)
# Print each character of a string.
 
for i in "Python world":
    print(i) 