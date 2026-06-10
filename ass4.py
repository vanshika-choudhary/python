# Print the following patterns:
# *****
# ****
# ***
# **
# *

for i in range(5,0,-1):
    for j in range(i):
        print("*",end="")
    print()

# 12345
# 1234
# 123
# 12
# 1

for i in range(5,0,-1):
    for j in range(1,i+1):
        print(j,end="")
    print()

# *
# **
# ***
# ****
# *****

for i in range(6):
    for j in range(i):
        print("*",end="")
    print()

# 00000
# 11111
# 22222
# 33333
# 44444

for i in range(5):
    for j in range(5):
        print(i,end="")
    print()

# 1
# 22
# 333
# 4444
# 55555

for i in range(1,6):
    for j in range(i):
        print(i,end="")
    print()

# 1
# 12
# 123
# 1234
# 12345

for i in range(1,6):
    for j in range(1,i+1):
        print(j,end="")
    print()