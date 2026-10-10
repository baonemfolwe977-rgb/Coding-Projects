# -*- coding: utf-8 -*-

def validate_grade(grade_input):
    # Check if the grade is valid (between 0 and 100)
    try:
        grade = float(grade_input)
        if 0 <= grade <= 100:
            return True, grade
        else:
            return False, None
    except ValueError:
        return False, None

def calculate_average(grade_list):
    # Calculate the average of a list of grades
    if not grade_list:
        return 0
    return sum(grade_list) / len(grade_list)

def find_highest_and_lowest_grades(grade_list):
    # Find the highest and lowest grades from list
    if not grade_list:
        return 0, 0
    return min(grade_list), max(grade_list)

def main():
    # List of subjects
    subjects = ['Math', 'English', 'Science']
    
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

    # Create empty lists to store student information
    all_student_names = []
    all_student_grades = []

    # Input student data
    for student_num in range(num_students):
        name = input(f"\nEnter the name of student {student_num + 1}: ")
        all_student_names.append(name)
        student_grades = []
        
        for subject in subjects:
            while True:
                grade_input = input(f"Enter {name}'s grade for {subject} (0-100): ")
                is_valid, grade = validate_grade(grade_input)
                if is_valid:
                    student_grades.append(grade)
                    break
                else:
                    print("Invalid grade! Please enter a number between 0 and 100.")
        
        all_student_grades.append(student_grades)

    # Display Results
    print("\n==================================================")
    print("STUDENT GRADE SUMMARY")
    print("==================================================")

    for i in range(num_students):
        name = all_student_names[i]
        grades = all_student_grades[i]
        
        print(f"\nStudent: {name}")
        print("--------------------")
        
        for j in range(len(subjects)):
            print(f"{subjects[j]}: {grades[j]:.2f}")
        
        avg = calculate_average(grades)
        print(f"Average: {avg:.2f}")

    # Class Statistics
    print("\n==================================================")
    print("CLASS STATISTICS")
    print("==================================================")

    for i in range(len(subjects)):
        subject_grades = [grades[i] for grades in all_student_grades]
        avg = calculate_average(subject_grades)
        low, high = find_highest_and_lowest_grades(subject_grades)
        
        print(f"\n{subjects[i]}:")
        print(f"Class Average: {avg:.2f}")
        print(f"Highest Grade: {high:.2f}")
        print(f"Lowest Grade: {low:.2f}")

if __name__ == "__main__":
    main()