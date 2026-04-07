# Tuple practice 
tup = ("bnanaa",True,67.4,"mango","orange")
# print the type of the tuple 
print(type(tup))
# Print the length Of the tuple 
print(len(tup))
# print values from the tuple 
print(tup[2])
# slicing in the tuple of the python 
print(tup[1:3])
# in negitive slicing in the py 
print(tup[-5:-1])
print(tup[-5:])

thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)
if "banana" in thistuple:
    print("banana ha tple ma")
else:
    print("wrong choice")

    # update of a tuple in py using list 
tu = ("M khuabib",2233,18,)
print(tu)
new = list(tu)
new[1]="zohaib"
tu = tuple(new)
print(tu)

# ubnpak the tuple by give the name of the values 
mytup = ("M khubaib",123,21)
name,rollno,age=mytup
print(name)
print(rollno)
print(age)
 
#  find the index in the tuple 
ind = (1,2,3,4,4,5,6,4)
print(ind)
print(ind.index(4))
# count the values by the fuction count in the tuple 
print(ind.count(4))