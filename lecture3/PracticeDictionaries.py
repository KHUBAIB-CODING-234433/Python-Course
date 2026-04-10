# Dictionaries in the python Explain it 
# import copy
user = {
    "name":"khubaib",
    "roll no":23,
    "class":"Bscs E2",
    "section":"Evening"
}
# value get with the help of the keys 
print(user["name"])
# print(user["use"]) error a hay ga agar dictionary ma value na milay too 
# .get()  ka method use kar kay 
print(user.get("name"))
# agr dictionaries kay andar key na ho to get error nahi day ga balke (none)day ga 
print(user.get("down","not found"))
# saray items ko loop kar zaraya access karna or saray items ko access karna 
stu = {"name":"salman","age":"45"}
for key, values in stu.items():
    print(key,"==",values)
# agar humein sirf values chahiya to .values() ka function lagay 
for values in stu.values():
    print(values)
# agar humien sirf keys chahiya tu keys ka function looop par lagay ga 
for keys in stu.keys():
    print(keys)
students_data = {
    "name":"Ali",
    "AGE":14,
    "city":"lahore"
    }
print(students_data)
students_data["name"]="Anas"
students_data["city"]="Karachi"
print(students_data)
# add items in the dictionaries [] Direct tariqa and the update method to the update value 
ss = {
    "name":"khubaib maqsood",
    "Rool no":23,
}
# hum is ma city add karrien gay with the help of square bracets 
ss["city"]="Lahore"
print(ss)
# update method ki maddad say add karna items koo 
ss.update({"street":"muhala umer town skp"})
print(ss)
# Remove the items in the dictionaries from the different ways fit .pop() ki madad say 
dic = {
    "name":"Khubaib",
    "city":"Sheikhupura",
    "age":12,
    "status":"student"
}
dic.pop("age")
print(dic)
# net pop ite, use kar aky last vala item nikalna 
last ={
    "name":"babar",
    "status":"batsman",
    "score":"100",
    "win rate":"50%"
}
# win rate ko ,popitems() ki madad say nikal dana \
last.popitem()
print(last)
# del key word ki madad say delete karna aik key ko 
del_key = {
    "name":"shah nawaz",
    "ststus":"wiket keepr",
    "performance":"50 drop catch in 100 matches"
}
del del_key["name"]
print(del_key)
# pori dictionary ko clear kar dana .clear() ki madad say 
del_key.clear()
print(del_key)
# last id del key word ki madad say pori dictionary ko hi remove kar dana 
del_dic = {
    "name":"Kasif",
    "design":"singer"
}
del del_dic 
# loop on the dictionaries are the given below questions 
loop = {
    "name":"khubaib",
    "Roll no":222232,
    "papers":"board of the intermediate"
}
for x,y in loop.items():
    print(x,y)
# list kay andar copy karnay kay tariqay go kay given below hein  
copy={
    "name":"khan",
    "adreas":"sheikhupura",
    "age":20
}
copy1 = copy.copy()
# ab ya copy ho gya ha copy1 kay andar dona ka result same hi ay ga 
print(copy)
print(copy1)
# agr AP KI Dictionary nested ha tu ap ya use nahi kar saktay 
import copy
patient ={
    "name":"Ali Raza",
    "test":["blood","x_rays","suger"]
}
patient_copy = copy.deepcopy(patient)
patient_copy["test"].append("Mri")
print(patient)
print(patient_copy)
# nested dixtionary or multilevel dictionaries in the python 
school = {
    "class":{
        "student1":{
            "marks":{
                "math":98,
                "biology":100,
                "physics":99,
                "chemistry":39
            }
        },
        "student2":{
            "marks":{
                 "math":98,
                "biology":10,
                "physics":79,
                "chemistry":36

            }
        },
         "student3":{
            "marks":{
                 "math":98,
                "biology":10,
                "physics":79,
                "chemistry":36
            }
         },
    }
}
print(school["class"]["student1"]["marks"]["biology"])
print(school["class"])
# dictionaries method in the python programing are the give below ab hum is nested if par saray methods laga kar dikkhaien gay 
# first student1 ki key nikalna 
print(school["class"]["student1"]["marks"].keys())


