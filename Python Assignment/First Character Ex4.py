
'''
 Write a Python program to access the first character of a string using 
index value.
'''

Character = input("Enter a Character: ")


if len(Character) > 0:  
    first_character = Character[0]
    print("First character of the string:", first_character)
else:
    print("The string is empty. No character to access.")


