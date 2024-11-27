'''
Practical Example: 1) Write a Python program to skip 'banana' in a list using the continue 
statement. List1 = ['apple', 'banana', 'mango']
'''

List=["Apple","Banana","Mango","Orange","Coconut"]

for i in List:
    if i=="Mango":
        continue
print(List)

