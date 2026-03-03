# practice of the list in the python 
# make a list and print these numbers 
a = ["khubaib",89,989,]
print (a[0])
a[0]="maqsood"
print(a[0])
a.append("000")
print(a)

fruits = ["mango","cherry","orange","bannana","apple"]
print(fruits[0])
print(fruits[-1])
# mutability in the lists 
fruits[0]="zaiqa"
print(fruits)

numbers = [10,20,30,40]
print(numbers)
# appned last par naya item lanay ka lia use hota ha 
numbers.append(50)
print(numbers)
# extend last par zyada item gornay ka lia use hota ha 
numbers.extend([60,70,80])
print(numbers)
# pop nikalnay ka lia use hota ha 
numbers.pop()
print(numbers)
# slicing from the positive numbers in the lists 
print(numbers[2:])

print(numbers[-5:])
print(numbers[::-1])
# arragement in the order 
numbers.sort()
print(numbers)
# reverse order scope in the python 
numbers.sort(reverse=True)
print(numbers)

