
'''
Practical Example 3: Write a Python program to find a specific string in the list using a simple 
for loop and if condition. 
'''


my_list = ['apple', 'banana', 'cherry','Mango']


target=input("Enter Target Name :")

for item in my_list:
    if item == target:
        print("f'{target}' found in the list!")
        break
else:
    print("f'{target}' not found in the list.")
