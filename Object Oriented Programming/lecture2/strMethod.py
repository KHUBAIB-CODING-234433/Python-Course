# car ki details by the str method
class Car:
    def __init__(self,model,brand):
        self.model=model
        self.brand=brand
    def __str__(self):
        return f"the car model is {self.model} and the brand is {self.brand}"
car1=Car("corolla","toyota")
print(car1)
class Book:
    def __init__(self,title,authors,pages):
        self.title=title
        self.authors=authors
        self.pages=pages
    def __str__(self):
         return f"{self.title}:{self.authors} and the total pages are {self.pages}"
book1=Book("Python crash course","khubaib Maqsood",500)
print(book1)
# task with the str methods 
class Task:
    task_completed = True
    task_name = "purchaze done"
    # def __init__(self,task_completed,task_name):
    #      self.task_completed = task_completed
    #      self.task_name = task_name
    def __str__(self):
        if self.task_completed == True:
            return f"[completed] : {self.task_name}"
        else:
            return f"[] : {self.task_name}"
task1=Task()
print(task1)
# student grade system in the python 
class Student:
    # name = "khubaib maqsood"
    # marks = 50
    # status = "fail"
    def __init__(self,name,marks,status):
        self.name=name
        self.marks=marks
        self.status=status
    def __str__(self):
        if self.marks >=50:
            return f"Student:{self.name} = status:{self.status} marks:{self.marks}"
        else:
            return f"Student:{self.name} = status:{self.status} marks:{self.marks}"
s1=Student("khubaib",40,"fail")
print(s1)
s2=Student("Ali",90,"Pass")
print(s2)
s2.name="saad"
print(s2)
# print(s1)