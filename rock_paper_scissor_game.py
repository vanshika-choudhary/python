import random as rn
print("we will have 5 rounds here")
upt=0
cpt=0
l=["rock","paper","scissor"]
for i in range(5):
    c_choice=rn.choice(l)
    choice=input("enter your choice btw rock,paper and scissor")
    if choice=="paper":
        if c_choice=="paper":
            print(c_choice,"tie")
        elif c_choice=="rock":
            print(c_choice,"you got one point")
            upt+=1
        else:
            print(c_choice,"computer got one point")
            cpt+=1
    if choice=="rock":
        if c_choice=="rock":
            print(c_choice,"tie")
        elif c_choice=="scissor":
            print(c_choice,"you got one point")
            upt+=1
        else:
            print(c_choice,"computer got one point")
            cpt+=1
    if choice=="scissor":
        if c_choice=="scissor":
            print(c_choice,"tie")
        elif c_choice=="paper":
            print(c_choice,"you got one point")
            upt+=1
        else:
            print(c_choice,"computer got one point")
            cpt+=1        
print(f"computer score is {cpt} and your score is {upt}")
if cpt>upt:
    print("you lose!! computer win")
elif cpt<upt:
    print("you win!!congrats")
else:
    print("its a tie!!!")
