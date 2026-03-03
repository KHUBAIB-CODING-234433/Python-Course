marks = int(input("Please type the marks"))
if marks >= 0 and marks <= 100:
    if marks > 60:
        if marks >79:
            if marks >89:
                print('A grade')
            else:
                print(" B grade")
        else:
            print("C grade")  
    else: 
        print("You are fail")
else:
    print("Please enter valid marks")  
    # Practice question related to the nested if statement
username = input("enter the user name")
if username == "Khubaib maqsood":
    password = input("enter the password")
    if password == "khubaib":
        print("succesfully login")
    else:
        print("correct the password")
else:
        print("acces denied")
        # ----------------------------------------
salery = int(input("enter the amount"))

if  salery >=50000:
     credits = int(input("enter the credit score"))
     if credits >=1000:
          houseown = input("enter the house own")
          if houseown == "yes":
                  print("you are elligible to loan")
          else:
                  print("please buy your own house")
          
     else:
                  print("please increase the credit card limit")   
else:    
                  print("you does not take the loan") 
# Leeap year or not leap year \
year = int(input("enter the year ="))
if year%4==0:
    if year%100==0:
        if year%400==0:
         print(F"{year} this is the leep year")
        else:
             print(f"{year} this is not a leap year")
    else:
         print(F"{year} this is not a leap year")
else:
         print(F"{year} this is not a leep year")
# age checker licince 
age_person = int(input("enter the age ="))
if age_person <=60 and age_person >=0:
   if age_person >= 18:
    is_licince = input("if licince yes/not =")
    if is_licince == "yes":
        if age_person >40:
            print("you are old Not able to drive")
        else:
         print("you can drive the car or the bike on the road")
    else:
        print("please driving licince banvao")
   else:
    print("you cannot drive in the road underage")
else:
 print("enter the age in the range of the input value")

# number checking by the nested if loop 
num = int(input("enter the number"))
if num >0:
  if num%2==0:
    print("this is a even number")
  else:
    print("this is the odd number but this is a positive number")
else:
  print("the number is the negitive number")
# attendence checker result with the help of the nested if 
attandencs = int(input("enter the number"))
if attandencs <= 100 and attandencs > 0:
    if attandencs >= 75:
        numbers = int(input("enter the subject marks"))
        if numbers >=70:
            if numbers >=80:
                if numbers >= 90:
                    print("A grade")
                else:
                    print("B Grade")
            else:
                print("C grade")
        else:
            print("Fail")
    else:
        print("your attendence is less than 75 percentage")  
else:
    print("please Enter the number in the range")  
#  online shoping discount showed by the nested if statement 
total_purchase = int(input("Enter the Amount"))    
is_membership = input("member ship or not the membership")
if total_purchase > 5000:
     if  is_membership == "yes":
       discount = 20/100
       print(f"member = yes dicount 20%")
     else:
          discount =10/100
          print(f"not a member discount is 10% ")
else:
        discount = 5/100
        print(f"the discount is 5% =")
discount_amount = total_purchase * discount
final_price = total_purchase - discount_amount
print(discount_amount)
print(final_price)
        
# fiz buz with the nested if 
inp = int(input("Enter the number"))
if inp%3==0 and inp%5==0:
    if inp%3==0:
        if inp%5==0:
            print("buzz")
        else:("not fizz or nor buzz")
    else:
        print("fizz")
else:
    print("fizz and buzz")

# number in which take the number and print posiive negitive or the zero 
numberd = int(input("Enter the number"))
if numberd>0:
    print("this is a positive number")
elif numberd <0:
    print("this is a negitive number")
else:
    print("this is a zero number")

ages = int(input("Enter the age"))
if ages>=18:
    print("you can vote")
else:
    print("you canot vote ")
    # 5 sa pura divide hota ha ka nai 


div_num = int(input("enter the number"))
if div_num%5==0:
    print("numb is divide")
else:
    print("number is not divide")
# voval number or not the voval number in the program 
char = input("Enter the charater")
if char =="a" or char =="e"or char =="i"or char == "o" or char == "u":
    print("the number you can add is a voval number")
else:
    print("the number is not the voval and this is constrant")

# make a ledder of the elif statement in the python 
days = int(input("enter the numbers ="))
if days == 1:
    print("monday")
elif days==2:
    print("tuesday")
elif days == 3:
    print("wednesday")
elif days ==4:
    print("thursday")
elif days ==5:
    print("Friday")
elif days == 6:
    print("saturday")
elif days ==7:
    print("sunday")
else:
    print("please enter the number between the 1 to 7")

# ------------------------------------ 
phla = int(input("Enter the first number ="))
dosra = int(input("Enter the second number ="))
tesra = int(input("enter the third number ="))
if phla>dosra and phla >tesra:
    print("First number is greater ha")
elif dosra>phla and dosra >tesra:
    print("second number is the greater than the other")
else:
    print("third number bara ha or winner ha")

# ------------------------------------------ 
username = input("Enter the name =")
if username == "khubaib maqsood":
    password = input("enter the password =")
    if password == "0347@khub":
        print("login succesfull")
    else:
        print("please correct the password")
else:
    print("please correct the user name")

# ------------------------------- 
balance = 10000
pin = int(input("Enter the pin"))
if pin==12345:
    print("option select karien")
    print("option 1 withdraw amount")
    print("check the balance")
    option = int(input("enter the input"))
    if option == 1:
       withdraw = int(input("enter the Amount"))
       if withdraw <=balance:
          remaining = balance - withdraw
          print(f"your remaining amount willbe {remaining}")
       else:
          print("your banlance is insuficent")
    elif option ==2:
           print(f"the balane is equal {balance}")
    else:
       print("please correct the option invalid option selected")
     
else:
  print("incorect pin")
# Army Recuirement System 
hieght = float(input("Enter the hieght ="))
if hieght >=5.7:
    age = int(input("Enter the age ="))
    if age<=25 and age>=18:
        weight = int(input("Enter the Weight ="))
        if weight>60:
            print("Congratulation You are Selected")
        else:
            print("your weight is not in the Range")

    else:
        print("your age is not match Rejected")
else:
    print("rejected ap ki hieght kam ha")

    # Credit Card system in the bank 
Creminal_record =input("Enter the Creiminal record")
if Creminal_record == "yes":
  print("criminal record")
else:
    salery = int(input("Enter the salery"))
    if salery >= 100000:
     loan = input("loan ha ya nahi")
     if loan == "yes":
        print("loan ha is lia ap ko silver card mila")
     else:
        print("ap ko gold card mila ap pa koi loan nahi ha")
    elif salery >=50000:
       loan = input("loan mila ka nai")
       if loan == "yes":
          print("rejected loan ki waja sa")
    #    else:
          print("ap ko silver card mil gya ha")
    else:
       print("Salery kam ha is lia koi loan nahi ha bhag gao")

door_status = input("Enter the input")
if door_status == "open":
    gaurd_status = input("Enter input the gaurd sleep or not")
    if gaurd_status == "sleep":
       password = int(input("Enter the password"))
       if password == 786:
          filename = input("Enter the filename")
          if filename == "seceret":
              bahir = input("Enter the window or the door")  
              if bahir == "window":
               print("your mission complete")
              else:
                 print("Door par Police khari thi")
          else:
             print("Mission failed file galat utha li ha")
       else:
          print("password wrong ha Alarm baj gaya")
    else:
     print("gaurd na pakar lia")
else:
    print("mission failed darvaza band ha")

    # University admission Portal in the python 
marks =  int(input("Enter the Marks Matric"))
if marks >=60:
    marks = int(input("Enter the Fsc Marks"))
    if marks >=60:
        feild_select = input("Enter the field")
        if feild_select == "Cs":
            marks = int(input("enter the math marks"))
            if marks >=90:
                print("admission granted")
            else:
                print("Sorry math ma numbers kam ayy hein")
        elif feild_select == "eng":
            phyics = int(input("enter the marks"))
            if phyics > 80:
                print("mubarak ho admission ho gya")   
            else:
                print("ap kay marks kam hein")
        else:
            print("ya field hamaray pass nahi ha")
    else:
        print("fsc kay marks kam hein ap kay")
else:
    print("ap kay marks materic ma kam hein")

# solved the Question using the nested if in the below 
iq_level = int(input("Enter the IQ Level ="))
if iq_level>=110:
    coding_score = int(input("Enter the coding score ="))
    if coding_score >=75:
     communication_score =int(input("Enter the Communication Score ="))
     if communication_score >=60:
        Project_score = int(input("Enter the Project Score ="))
        if Project_score >=70:
           experience = int(input("Enter the Experienced ="))
           if experience >=2:
              income = int(input("Enter the income ="))
              if income <= 20000:
                 print("Full Elite")
              else:
                 if income <= 40000:
                    print("half alite")
                 else:
                    print("no scholarship")
           else:
              if experience < 2:
                 print("Selected(No Elite)")
        else:
           print("Rejected")
     else:
        print("Rejected")
    else:
        print("Rejected")
else:
    print("Rejected")






        

    

    
    



