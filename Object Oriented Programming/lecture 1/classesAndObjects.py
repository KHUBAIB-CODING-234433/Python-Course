# claas and the objects 
class Car:
    color="red"
    model="2024"
c1=Car()
print(c1.color)
print(c1.model)
c2=Car()
print(c2.color)
print(c2.model)
# init method self parameter an change data in objects etc learned 
class Laptop:
    def __init__(self,company,ram):
        self.company = company
        self.ram = ram
    def information(self):
         print(f"ya {self.company} ka laptop ha our {self.ram}")
comp = Laptop("HP","128gb")
print(comp.ram)
print(comp.company)
comp.information()
comp.company="lenovo"
comp.information()
comp1 = Laptop("dell","256gb")
print(comp1.ram)
print(comp1.company)
comp2 = Laptop("asus","512gb")
print(comp2.ram)
print(comp2.company)
comp1.information()
comp1.ram = "512gb"
comp1.information()
# student information print in this way of the object
class student:
    def __init__(self,name,rollno):
        self.name = name
        self.rollno = rollno
s1=student("khubaib",12)
print(s1.name)
print(s1.rollno)
# find the rectangular area of the rectangle using class and object by the return method in py
class rectangle:
    def __init__(self,length,width):
        self.length = length
        self.width = width
    def area(self):
        return self.length*self.width
r1 = rectangle(10,5)
print(r1.area())    
# find the rectangular area of the rectangle using class and object
class rectangle:
    def __init__(self,length,width):
        self.length = length
        self.width = width
    def area(self):
        return self.length*self.width
r1 = rectangle(10,5)
print(r1.area()) 
# make the simple counter using the classes and the objects 
class  counter:
    def __init__(self):
        self.count = 0
    def increment(self):
        self.count = self.count +1
    def reset(self):
        self.count = 0
mycounter=counter()
mycounter.increment()
mycounter.increment()
mycounter.increment()
print(mycounter.count)
mycounter.reset()
print(mycounter.count)
# student grading system simple logic pass or fail
class Student:
    def __init__(self,name,number):
        self.name=name
        self.number=number
    def grade(self):
        if self.number<50:
            print(f"{self.name} has {self.number} numbers and becomes fail")  
        else:
            print(f"{self.name} has {self.number} numbers and becomes pass")  
s1=Student("khubaib",45)
s1.grade()
s2=Student("ali",75)
s2.grade()
# python greating program using class and object
class Greating:
    def __init__(self,name):
        self.name=name
    def say_hallo(self):
        print(f"Hallo {self.name} welcome to python programming")
    def say_goodbye(self):
        print(f"Goodbye {self.name} see you later")
g1=Greating("khubaib")
g1.say_hallo()
g1.say_goodbye()
# crate a calculator using class and object in python
class Calculator:
    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2
    def add(self):
        return self.num1 + self.num2
    def subtract(self):
        return self.num1 - self.num2
    def multiply(self):
        return self.num1 * self.num2
    def divide(self):
        if self.num2 != 0:
            return self.num1 / self.num2
        else:
            return "Cannot divide by zero"
calc = Calculator(10, 5)
print("Addition:", calc.add())
print("Subtraction:", calc.subtract())
print("Multiplication:", calc.multiply())
print("Division:", calc.divide())
# happy birth say celeberarion using class and object in python
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def celebrate_birthday(self):
    self.age += 1
    print(f"Happy birthday!{self.name} You are now {self.age}")

p1 = Person("khubaib", 25)
p1.celebrate_birthday()
p1.celebrate_birthday()


