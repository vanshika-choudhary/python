#Tuple
# Check whether a given value exists in a tuple.
t1=(1,2,3,4,5,5,5)
print(3 in t1)
# Count how many times a specific element appears in a tuple.
print(t1.count(5))
# Find the index position of a given element.
print(t1.index(4))
# Iterate through a tuple using a loop and print all elements.
for i in t1:
    print(i)
# Create a single-element tuple and verify its type.
t2=(23,)
print(type(t2))
# Reverse a tuple.
print(t1[::-1])
# Convert a tuple into a list.
l1=[]
for i in t1:
    l1.append(i)    #or use list(t1)
print(l1)
# Convert a list into a tuple.
t2=tuple(l1)
print(t2)
# Concatenate two tuples and print the result.
t3=(3,4,5)
t4=(6,7,8)
print(t3+t4)
# Repeat a tuple 4 times using an operator.
print(t3*4)
# Swap the first and last element of a tuple.  
l3=list(t3)
a=l3[0]
b=l3[-1]
l3[-1]=a
l3[0]=b
print(tuple(l3))
# Find the frequency of each element in a tuple.
for i in t3:
    print("the frequency of",i,"is",t3.count(i))
# #Sets
# Create a set containing 8 numbers. Add two new numbers and print the updated set.
s1={10,50,37,58,35,83,56,11}
s1.update([99,77])
print(s1)
# Create an empty set and add 5 values one by one.
s2=set()
s2.add(23)
s2.add(57)
s2.add(33)
s2.add(90)
s2.add(60)
print(s2)
# Add multiple values to a set in a single statement.
s2.update([39,25])
print(s2)
# Create a set and remove an existing element. Print the result.
s2.remove(39)
print(s2)
# Find the elements that are present in Set A but not in Set B.
seta={1,2,3,4,5}
setb={4,5,6,7,8}
print(seta.difference(setb))
# Find the elements that are present in Set B but not in Set A.
print(setb.difference(seta))
# Find elements that are present in either Set A or Set B but not in both.Create a set of city names and check whether a given city exists.
print(seta.symmetric_difference(setb))
# Merge three different sets and count the total unique elements.
setc={8,9,10,11,12}
setd=seta.union(setb,setc)
print(len(setd))