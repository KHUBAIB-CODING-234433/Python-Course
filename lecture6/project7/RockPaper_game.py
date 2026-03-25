import random
item_list = ["Rock","paper","sciesor"]
usercoice=input("Enter the Choice =")
comp_choice =random.choice(item_list)
print(f"user choice is {usercoice}")
print(f"computer choice is {comp_choice}")
if usercoice == comp_choice:
    print("both choice are the same match tie")
elif usercoice == "rock":
    if comp_choice == "paper":
        print("paper covers rock == computer wins")
    else:
        print("rock break the seasor so the == we wins ")
elif usercoice == "paper":
    if comp_choice == "sciesor":
        print("sciesor cut the paper == computer wins")
    else:
        print("paper covers rock == we win")
elif usercoice == "sciesor":
    if comp_choice =="paper":
        print("sciesor cut the paper ==we win")
    else:
        print("rock break the seasor so the == computer wins ")
else:
    ("invalid input")




