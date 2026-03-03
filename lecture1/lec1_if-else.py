# if and else and el if complete questions
temp = 35
if temp > 30:
    print("its hot today and the tempurature is", temp)
# --------------------------------------------
score = 100
if score == 100:
    print("this is a perfect score")
    # -----------------------------------------------
status = "online"
if status == "online":
    print("the user becomes online")
    # -----------------------
speed = 89
if speed >= 70:
    print("speed becomes very high")
# --------------------------------
is_game_over = True
if is_game_over ==True:
    print("game is oveer plese restart")
# ----------------------------------------
age = 25
is_licince = True
if age>=18 and is_licince == True:
    print("you can drive the car on the road")
# -------------------------------------------
color = "red"
if color == "red" or color == "blue":
    print("your color is red")  
    # -------------------------------------
voval = ["a","e","i","o","u"]
letter = "s"
if letter in voval:
    print("the letter is a volval")
else:
    print("leter not found")
    # ------------------------
tempurature = 25
if tempurature > 20:
    print("its warm")
    if tempurature < 30:
        print("its hot today") 
# ---------------------------------- 
numb = 14
if numb %2==0:
    print("the number is a even number")  
#  ------------------------------------ 
is_login = True
is_admin = True
if is_login:
    if is_admin:
     print("acees granted")      
    #  if and else questions 
age = int(input("Enter the age ="))
if age >=18:
    print("you are elligible to the vote")
else:
    print("you are not elligible for the vote")
# ---------------------------------------
password = input("Enter the password")
if password == "0347@khub":
    print("sign in successful")
else:
    print("acces denied wrong password")
# ----------------------------------------------
check_even = int(input("enter the number"))
if check_even%2 ==0:
    print("even number")
else:
    print("odd number")
# -------------------------------------- 
num12 = int(input("Enter the number ="))    
if num12 < 0:
    print("negitive number")
elif num12 >0:
    print("number is positive")
else:
    print("the number is zero")
# -------------------------------------- 
# loop in the python while looopfruits = ["apple", "banana", "cherry"]
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)



