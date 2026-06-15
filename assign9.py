# 1. Student Result System
# student = {
#     "name": "Aman",
#     "roll_no": 101,
#     "marks": 420,
#     "total_marks": 500
# }
# Tasks:
# Print the student's name.
# Print marks and total marks.
# Calculate the percentage.
# Add a new key "grade" based on the percentage.
# Display all details using a loop.
 
student = {
    "name": "Aman",
    "roll_no": 101,
    "marks": 420,
    "total_marks": 500
}
print(student["name"])
print(student["marks"])
print(student["total_marks"])
percent=(student["marks"]/student["total_marks"])*100
print(percent)
if percent>90:
    student.update({"grade":"A"})
elif percent>50 and percent<=90:
    student.update({"grade":"B"})
else:
    student.update({"grade":"C"})
print(student["grade"])

for key , value in student.items():
    print(key,value)
    
# Company Employees (Nested Dictionary)
# employees = {
#     "emp1": {
#         "name": "Aman",
#         "salary": 50000
#     },
#     "emp2": {
#         "name": "Krish",
#         "salary": 60000
#     }
# }
# Tasks:
# Print the salary of emp1.
# Print the name of emp2.
# Increase emp1's salary by 5000.
# Add "experience" to emp2.
# Print all employee details.

employees = {
    "emp1": {
        "name": "Aman",
        "salary": 50000
    },
    "emp2": {
        "name": "Krish",
        "salary": 60000
    }
}
print(employees["emp1"]["salary"])
print(employees["emp2"]["name"])
employees["emp1"]["salary"]+=5000
employees["emp2"]["experience"]="experienced"
for key,value in employees.items():
    print(key)
    for key1,value1 in value.items():
        print(key1,value1)

# Create a dictionary of 5 products and their prices. Find the most expensive product.
d1={"vaseline":300, "biscuits":30, "bread":50, "mangoes":100, "lipgloss":500}
print(max(d1))

# Create a dictionary of subjects and marks. Calculate total marks and average marks.
d2={"maths":36,"eng":99,"science":45,"sst":79}
total_marks=0
for i in d2.values():
    total_marks+=i
print("total marks:",total_marks)
print("average marks:",total_marks/4)

# Create a report card system using a nested dictionary and print the percentage of each student.
d3={"std1":{"name":"moni","rollno":100,"percent":55},"std2":{"name":"hansika","rollno":102,"percent":77},
    "std3":{"name":"tarishi","rollno":104,"percent":99},"std4":{"name":"vanshika","rollno":106,"percent":100}}
for key,value in d3.items():
    print(key)
    for key1,value1 in value.items():
        print(key1,value1)
for student, details in d3.items():
    print(details["name"], ":", details["percent"], "%")

# List Comprehension
# Create a list containing numbers from 10 to 30.    
numbers = [i for i in range(10, 31)]
print(numbers)

# Create a list containing the length of each word.   
# words = ["python", "java", "cpp",'data Science]

words = ["python", "java", "cpp", "data Science"]

lengths = [len(word) for word in words]
print(lengths)

# Create a list containing numbers divisible by both 2 and 3 between 1 and 50.  

divisible = [i for i in range(1, 51) if i % 2 == 0 and i % 3 == 0]
print(divisible)
# Create a list containing:                             
# "Pass" if marks are greater than or equal to 40
# "Fail" otherwise
marks = [35, 78, 40, 22, 90, 39]

result = ["Pass" if mark >= 40 else "Fail" for mark in marks]
print(result)
