dics ={
    "name" : "khubaib",
    "roll no":4500,
    "class":12,
    "subject":["English","math","computer","Biology","Urdu"],
    "isadmit":True,
    "tup":("junuary","Feburary","March","Aprail","May"),
    "sub_marks":{
        "Engish":98,
        "math":98,
        "computer":87,
        "biology":97,
        "Urdu":100
    }
    
}
# for print only one value from the dictionary 
print(dics["sub_marks"])
# length of the dicrionaries 
print(len(dics))
# Type of the dictionaries 
print(type(dics))
# put the values in the valriable 
car = {
    "brand":"Ford",
    "model":"mustang",
    "year":1988,
}
print(car["brand"])
print(len(car))
print(type(car))

# use dictionary method to make the dictionary 
dicso = dict(name="khubaib",age = 19,school="muslim model high school sheikhupura")
print(dicso)
# change the items of the Dictionary 
car = {
    "brand":"Ford",
    "model":"mustang",
    "year":1988,
}
print(car)
car["brand"]="lamberini"
car["model"]="sonata"
car["year"]=2023
print(car)
# update the values using the update method 
car.update({"year":"2025"})
print(car)
# update items in the dictionaries practice questions 
car = {"brand": "Honda", "model": "Civic", "year": 2018}
car["year"]=2025
print(car)
# new key value pair add karna 
car.update({"brands":"alto"})
print(car)
# value ma add karna ka vo 10 add ho kar 60 ho gay 
scores = {
    "Ali": 50, 
    "Bilal": 45
}
scores["Ali"]=scores["Ali"]+10
print(scores)
# methods in the Dictionaries Clear() also del key word jo pura var hi uda data ha
student_info = {
    "name": "Ali",
    "age": 20,
    "grade": "A"
}
print(f"clear karnay say pahlay {student_info}")
student_info.clear()
print(f"clear karnay kay bad {student_info}")
del student_info
print(f"student info delete ho gai ha {student_info}")
