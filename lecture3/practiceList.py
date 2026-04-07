fruits = ["apple","mango","cherry","orange","Watermelon","banana"]
print(fruits[0])
print(fruits[1])
print(fruits[-1])
print(fruits[-2])
print(fruits[0:])
print(fruits[0:4])
print(fruits[-3:-6:-1])

# items add karnay vala function append()
fruits.append("strawbery")
print(fruits)
# list ma pni marzi KAY  index par new items add karna insert()
fruits.insert(2,"mangoes")
print(fruits)
# list ko (extend) karnay vala function is ma list kay sath agar koi or list laganai ho tu lag agati ha 
vegetable = ["gobi","alo","mater"]
fruits.extend(vegetable)
print(fruits)
# items ko delete or nikalnay valay function remove()
fruits.remove("gobi")
print(fruits)
# nested list comprehension 
matrix = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12]
]
# trans=[[row[i] for row in matrix] for i in range(4)]
# print(trans)
 
#  dosra tariqa 
 
# transposed = []
# for i in range(4):
#     transposed_row =[]
#     for row in matrix:
#         transposed_row.append(row[i])
#     transposed.append(transposed_row)
# print(transposed)

# third and the shotest way by zip function 
zop=list(zip(*matrix))
print(zop)

# loop on the lists 
fruits = ["apple","mango","grapes"]
for fruit in fruits:
    print(fruit)

# values kay sath agar index bi chahya 
vege = ["carrot","apple","mango"]
for index,vegetable in enumerate(vege):
    print(index,vegetable)

# list ko copy karna 
original = ["apple","mango","cherry"]
new = original.copy()
new.append("saib")
print(original)
print(new)

# tuple join karna 
tup = ("hallo","ya","aik","python","ha")
tup_join = ", ".join(tup)
print(tup_join)

fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2
print(mytuple)

# sets ki practice 
mera_set ={"a","b","c","d","e","e"}
print(mera_set)
# sets kay andar say items ko access karna 
mera_set ={"aple","cherry","Orange"}
for set in mera_set:
    print(set)
print("aple"in mera_set)
print("aple" not in mera_set)
# add the set items in the python 
# ek item add karnay ka lia add methhod 
mera_set.add("banana")
print(mera_set)
# aik say zyada items add karnay ka lia update method 
mera_set.update(set)
print(mera_set)
print(sorted(mera_set))
