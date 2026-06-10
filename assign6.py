# Question
# Create a list containing:
# integers
# strings
# floating values
# Requirements:
# Print the third element of the list.
# Print elements from index 1 to index 4 .
# Replace one element with a new value.
# Print the updated list.

l1=[1,2,3,"hi","bye",5.4,3.4]
print(l1[2])
print(l1[1:5])
l1[2]=4
print(l1)

# Question
# Create a list of student marks.
# Requirements:
# Add a new mark using append().
# Add multiple marks.
# Insert a mark at index 2.
# Print the final list

l2=[34,56,78,69,90]
l2.append(58)
l3=[70,50]
l2.extend(l3)
l2.insert(2,66)
print(l2)

# # Question
# Create a list of product names.
# Requirements:
# Remove one product using remove.
# Remove the last product.
# Print the removed product.
# Display the updated product list.

l4=["dot and key","foxtale","dermaco","vlcc"]
l4.remove("foxtale")
print(l4.pop())
print(l4)

# Question
# Create a list of movie names.
# Requirements:
# Add 3 new movies.
# Insert your favorite movie at the beginning of the list.
# Print the complete movie list.
# Display the total number of movies .

l5=["avengers infinity war","dhurandhar","thor the ragnork","spiderman"]
l6=["doctor strange","the drama","drifting home"]
l5.extend(l6)
l5.insert(0,"steel of troops")
print(l5)
print(len(l5))

# Question
# Create a list of numbers entered by the user.
# Requirements:
# Sort the list in ascending order.
# Sort the list again in descending order.
# Print both outputs.

l7=[]
n=int(input("enter no of items you want to print"))
for i in range(n):
    i1=input()
    l7.append(i1)
l7.sort()
print(l7)
l7.sort(reverse=True)
print(l7)


    