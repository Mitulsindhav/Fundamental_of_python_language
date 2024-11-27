'''
Practical Example 7: Write a Python program to calculate grades based on percentage using 
if-else ladder. 
'''

sname=input("Enter Student Name :")
rollno=int(input("Enter Roll No :"))
sub1=int(input("Enter Marks of Subject 1 :"))
sub2=int(input("Enter Marks of Subject 2:"))
sub3=int(input("Enter Marks of Subject 3:"))

total=sub1+sub2+sub3
per=total/3

print("Student Name:",sname)
print("Roll No:",rollno)
print("Total :",total)
print("percentage:",per)

if per>=80:
    print("Distriction")
elif per>=70:
    print("First Class")
elif per>=50:
    print("Second class")
elif per>=40:
    print("Pass")
else:
    print("Fail")


