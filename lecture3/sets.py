# Frozen sets in the python 
x = frozenset(["apple","cherry","banana"])
print(x)
print(type(x))
# copy() method ki madad say copy karna frozen set ko copy karna and union 
a = frozenset([1,2,3,4])
b = frozenset([5,6,7,8])
c = a.copy()
print(c)

print(a.union(b))
# intersection of the sets in the python 
print(a.intersection(b))
# Difference of the sets in the python 
# print(a-b)
print(a.difference(b))
# symmeteric differnce in the python ot the use of the ^ for the symmeteric difference 
print(a.symmetric_difference(b))
# issubset() in the python programming language or the <=
x = frozenset([1,2])
print(x.issubset(a))
# print(x <= b)
# issuperset in the python programming or the >= is the sign 
print(a.issuperset(x))
# is sdisjoint set in the python programming 
print(a.isdisjoint(b))
# Real world problem in which the problem of the sets all methods are the worked with this 
front_req = frozenset(["Html","css","java script","React"])
backend_req = frozenset(["python","django","java script","node.js"])
# union kar kay sari ko sath milana ta ka sari fields ikathi ho sakien 
print(front_req|backend_req)
# common nikalnay kay lia company ko data lana ha ka kon si language front or back dono use kartay hein
print(front_req&backend_req)
# difference maloom karnay ka lia ka backend ma move karnay ka lia kya skill sikhni hoo gi 
print(backend_req-front_req)
# symeterical differnce comman nikal gay or bali idar a jaien 
print(front_req ^ backend_req)

# comparision method in the python using the frozen set return true or the false 

ali_skill = frozenset(["Html","css","java script","React","git"])
print(front_req.issubset(ali_skill))
# super set in the following 
print(ali_skill.issuperset(front_req))

