
def calculate_average(grades):
    return sum(grades) / len(grades)


def assign_letter_grade(average):
    if average >= 90:
        return 'A'
    elif average >= 80:
        return 'B'
    elif average >= 70:
        return 'C'
    elif average >= 60:
        return 'D'
    else:
        return 'F'


def input_grades_and_calculate():
    name = input("Enter the student's name: ")
    
    grades = []
    num_grades = int(input("How many subjects does the student have? "))
    
    for i in range(num_grades):
        grade = float(input(f"Enter grade for subject {i+1}: "))
        grades.append(grade)
    
    average = calculate_average(grades)
    letter_grade = assign_letter_grade(average)
    
    print(f"\nStudent: {name}")
    print(f"Grades: {grades}")
    print(f"Average: {average:.2f}")
    print(f"Letter Grade: {letter_grade}\n")


def main():
    while True:
        print("Grade Management System")
        print("1. Enter grades for a student")
        print("2. Exit")
        
        choice = input("Enter your choice (1 or 2): ")
        
        if choice == '1':
            input_grades_and_calculate()
        elif choice == '2':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice, please enter 1 or 2.")
        
        print("-" * 30)


if __name__ == "__main__":
    main()
