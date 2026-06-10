# Create a string "Python Programming" and print:
# First character
# Last character

a="pyhton programming"
print(a[0])
print(a[-1])

# Create a string "Data Science" and print the first 4 characters using slicing.

b="Data Science"
print(b[:4:])

# Print every second character from the string "Machine Learning".

c="machine learning"
print(c[::2])

# Convert the string "hello world" to uppercase.

d="hello world"
print(d.upper())

# Convert the string "PYTHON" to lowercase.

e="PYTHON"
print(e.lower())

# Capitalize the string "python programming".

f="pyhton programming"
print(f.capitalize())

# Find the length of the string "Artificial Intelligence".

g="Artificial Intelligence"
print(len(g))

# Check whether the string "Python" starts with "Py".

h="Python"
print(h.startswith("Py"))

# Check whether the string "Python" ends with "on".

print(h.endswith("on"))

# Print each character of the string "Developer" using a for loop.

i="Developer"
for j in i:
    print(j)

# Remove extra spaces from the string " Data Analytics ".

j=" Data Analytics "
print(j.strip())

# Join two strings "Data" and "Analytics" with a space between them.

k="Data" + " " + "Analytics"
print(k)

# Reverse the string "Python" using slicing.

l="python"
print(l[-1::-1])

# Count how many times the string "Hello" is repeated when multiplied by 5.

k="Hello"
l=(k*5)
print(len(l)//len(k))

# Print all characters of "Programming" except the first and last character.

m="Programming"
print(m[1:-1:])

# Extract "world" from the string "Hello world" using slicing.

n="Hello world"
print(n[6::])

# Check whether "12345" contains only digits.

o="12345"
print(o.isdigit())

# Check whether "PythonDS" contains only alphabets.

j="PythonDS"
print(j.isalpha())

# Print the last element of the list.

l1=["l1","l2","56","89"]
print(l1[-1])

# Print the first three elements using slicing.

print(l1[:3:])

# Print every second element from the list.

print(l1[::2])

# Print all elements except the first element.

print(l1[1::])