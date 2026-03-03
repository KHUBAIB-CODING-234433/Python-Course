# While loop peactice question 
# print numbers from 1 to 5 
i = 1
while i <= 5:
    print(i)
    i=i+1
# reverse order print 
j = 5
while j>=1:
    print(j)
    j=j-1
# even number print 
e = 2
while e<=10:
    print(e)
    e = e+2
s = 1
sum = 0
while s<=5:
    sum = sum+s
    s=s+1
print(sum)


i = 1
total = 0
while i <= 5:
    total = total + i
    i = i + 1
print("Total Sum:", total)

# print the values and its square of the value 
m = 1
while m <=5:
    print(f"{m} and the square of the value is {m*m}")
    m =m+1

# input a number and display a table in the python 
table_num = int(input("Enter the number you can want"))
table = 1
while table <=10:
    print(f"{table_num} x {table} = {table*table_num}")
    table = table +1


x = int(input("Enter the number in the string ="))
sum =0
a=x
while x != 0:
    reminder = x%10
    if reminder==0:
        sum =sum + x
    else:
        sum = sum + reminder
    x=x//10
print(f"the sum of the values of {a} is {sum}")

# find the factorial of the input 
n = int(input("Enter the number"))
c=1
f=1
while c<=n:
    f = f*c
    c=c+1
    print(f"the factorial of {n} is {f}")

# advance concpts in the while loop and solved the question 
search = 1
target = 7
while search <= 5:
    if search == target:
        print("number mil gya ")
        break
    search=search +1
else:
    print("loop ka andar number nai mila ")

# practice in the loop 
isrunning = True
attempt = 1
while isrunning ==True and attempt <= 3:
    inp = input("Enter the input in the program")
    if inp == "Quite":
        isrunning == False
    elif inp == "seceret123":
        print("Accces Granted")
        isrunning = False
    else:
        attempt = attempt +1
        print(f"Wrong password attemp are {attempt-1}")

# nested loop in the python 
     
i = 1
while i <=5:
    j=1
    while j<=5:
        print(f"the rows are {i} and the columns are {j}")
        j=j+1
    print("")
    i = i+1

import random

print("--- Number Guessing Game ---")
print("Maine 1 se 10 ke darmiyan ek number socha hai.")

# Computer ne secret number soch liya
secret_number = random.randint(1, 10) 

# Hamare counters
attempts_taken = 0
max_attempts = 3
# Game ka main loop shuru
while attempts_taken < max_attempts:
    # User se input lena aur usay number (integer) mein badalna
    user_guess = input(f"\nAttempt {attempts_taken + 1} - Koi number guess karein (1-10): ")
    guess = int(user_guess) 

    # --- CONTINUE KA USE ---
    # Agar user ghalti se 10 se bada ya 1 se chota number daal de
    if guess < 1 or guess > 10:
        print("Dhyan se! Number 1 aur 10 ke darmiyan hona chahiye. Yeh attempt count nahi hoga.")
        continue  # Loop ko wahi rok kar wapas upar bhej dega (attempt count nahi hoga)

    # Agar number valid hai, toh hum attempt ko count kar lenge
    attempts_taken += 1

    # --- BREAK KA USE ---
    # Agar user jeet gaya
    if guess == secret_number:
        print(f" Zabardast! Aapne sahi pehchana. Secret number {secret_number} hi tha!")
        break  # Game jeet li, isliye loop ko foran tod do
        
    # User ki madad ke liye chotay hints
    elif guess < secret_number:
        print("Aapka guess thora chota hai. Koi bada number sochein.")
    else:
        print("Aapka guess thora bada hai. Koi chota number sochein.")

# --- ELSE KA USE ---
# Yeh tab chalega jab loop apne 3 attempts poore kar lega aur 'break' nahi hoga
else:
    print(f"\nGame Over! Aapke 3 attempts khatam ho gaye. Secret number {secret_number} tha.")

# beeginer level loop question 
# print the number from the 1 to 5
i = 1 
while i <= 5:
    print(i)
    i = i+1
# print the sum of the numbers 
i = 1 
total = 0 
while i <=10:
   total =total +i
   i=i+1
   print(f"the sum of the {i} = {total}")   
   
    













