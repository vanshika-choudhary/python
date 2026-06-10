# 1. Restaurant Ordering System
# Question
# Create a restaurant ordering system using an infinite loop.
# Requirements:
# Display the following menu:
# Pizza → ₹200
# Burger → ₹120
# Pasta → ₹150
# Ask the user to enter an item name.
# If the item exists, add its price to the total bill.
# Otherwise display:
# "Item not available"
# Ask the user:
# "Do you want to order more? (yes/no)"
# If the user enters "no", stop the program.
# Display the final bill amount.

print("we have following items in our menu:")
print(" Pizza → ₹200")
print("Burger → ₹120")
print("Pasta → ₹150")

bill=0
while True:
    item=input("enter an item:")
    if item=="pizza" or item=="Pizza":
        bill+=200
    elif item=="burger" or item=="Burger":
        bill+=120
    elif item=="pasta" or item=="Pasta":
        bill+=150
    ord=input("if you want to order more?(yes/no)")
    if ord=="yes" or ord=="Yes":
        continue
    else:
        break    
print("your bill is",bill)

# 2. Password Verification System
# Question
# Create a password verification system using while True.
# Requirements:
# Correct password:
# "Python@123"
# Continuously ask the user to enter the password.
# If the password is incorrect, display:
# "Wrong Password"
# If the password length is less than 5 characters, display:
# "Password too short"
# If the password is correct:
# "Login Successful"
# and stop the loop.

while True:
    pas=input("enter the password:")
    if pas=="Python@123":
        print("Login succesfully!!")
        break
    elif len(pas)<5:
        print("Password too short!!")
    else:
        print("wrong password!!!")