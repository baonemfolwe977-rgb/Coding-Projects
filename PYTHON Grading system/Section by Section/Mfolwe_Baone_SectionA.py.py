def validate_grade(grade_input):
    try:
        grade = float(grade_input)
        if 0 <= grade <= 100:
            return True, grade
        else:
            return False, None
    except ValueError:
        return False, None

def main():
    # Get the number of students
    while True:
        try:
            num_students = int(input("Enter the number of students in the class: "))
            if num_students > 0:
                break
            else:
                print("Please enter a positive number.")
        except ValueError:
            print("Please enter a valid number.")

    #store student data
    student_grades = {}

    # Input student data
    for i in range(num_students):
        name = input(f"\nEnter the name of student {i + 1}: ")
        
        # Grade validation loop
        while True:
            grade_input = input(f"Enter {name}'s grade (0-100): ")
            is_valid, grade = validate_grade(grade_input)
            
            if is_valid:
                student_grades[name] = grade
                break
            else:
                print("Invalid grade! Please enter a number between 0 and 100.")

    # Calculate statistics
    total_grade = sum(student_grades.values())
    average_grade = total_grade / num_students

    # Display Results
    print("\n==================================================")
    print("STUDENT GRADE SUMMARY")
    print("==================================================")

    # Show each student's grade
    for name, grade in student_grades.items():
        print(f"\nStudent: {name}")
        print(f"Grade: {grade:.2f}")

    # Show class statistics
    print("\n==================================================")
    print("CLASS STATISTICS")
    print("==================================================")
    print(f"Class Average: {average_grade:.2f}")
    print(f"Highest Grade: {max(student_grades.values()):.2f}")
    print(f"Lowest Grade: {min(student_grades.values()):.2f}")

# Run the main program
if __name__ == "__main__":
    main()
