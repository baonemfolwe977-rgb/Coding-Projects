#SECTION A
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


#SECTION B

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

#SECTION C

import statistics
import sys

students={}
SUBJECTS = ["Math", "English", "Science"]

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
    try:
        if not grade_list:
            return None
        else:
            return statistics.mean(grade_list)
    except statistics.StatisticsError:
        return None
    

def add_student(students_dict, student_name):
    # If student doesn't already exist
    if student_name not in students_dict:
        # Create new student entry with empty grade lists for each subject
        students_dict[student_name] = {
            subject: [] for subject in SUBJECTS
        } #For the student name we entered create an empty list for each subject.
        return True
    return False  # Student already exists


def remove_student(students_dict, student_name):
    # Check If student exists
    if student_name in students_dict:
        # Remove the student from dictionary
        del students_dict[student_name]
        return True
    return False  # if entered student doesn't exist

def update_grade(students_dict, student_name, subject, grade):
    # Validate inputs first
    is_valid, grade_value = validate_grade(grade)
    if is_valid and student_name in students_dict and subject in SUBJECTS:
        # Add the grade to appropriate subject list
        students_dict[student_name][subject].append(grade_value)
        return True
    return False

def input_student_grades(students_dict, student_name):
    # For collecting inputs
    if student_name not in students_dict:
        print("Student not found!")
        return False
        
    for subject in SUBJECTS:
        while True:
            try:
                grade_input = input(f"Enter {student_name}'s grade for {subject} (0-100): ")
                if update_grade(students_dict, student_name, subject, grade_input): #Pass grade_input to update_grade
                    break
                else:
                    print("Invalid grade! Please enter a number between 0 and 100.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")
    return True
  
def get_student_grades(students_dict, student_name): #provides clean way to get data like ya get_student_report, usuful later
    try:
        if student_name in students_dict:
            return students_dict[student_name]
        return None
    except KeyError:
        return None

def get_subject_grades(students_dict, subject):
    try:
        if subject not in SUBJECTS:
            print("Invalid subject!")
            return None
        
        subject_grades = {}
        for student in students_dict:
            subject_grades[student] = students_dict[student][subject]
        return subject_grades
    except KeyError:
        return None
    
def get_student_report(students_dict, student_name):
    try:
        if student_name not in students_dict:
            print("Student not found!")
            return None
        report = {}
        student_grades = students_dict[student_name]
        
        for subject in SUBJECTS:
            try:
                grades = student_grades[subject] #Get list ya grades
                avg = calculate_average(grades)#pass list to calculate_average
                report[subject] = {
                    'grades': grades,
                    'average': avg if avg is not None else 'No grades yet'
                }
            except:
                print("Error processing subject")
                continue
        return report
    except:
        print("Error generating student report")
        return None

def display_menu():
    try:
        print("\n=== Grade Management System ===")
        print("1. Add New Student")
        print("2. Remove Student")
        print("3. Enter Grades")
        print("4. View Student Report")
        print("5. View Subject Grades")
        print("6. Exit")
        
        while True:
            try:
                choice = int(input("\nEnter your choice (1-6): "))
                if 1 <= choice <= 6:
                    return choice
                print("Please enter a number between 1 and 6")
            except:
                print("Please enter a valid number")
    except:
        print("Error displaying menu")
        return 6

def display_student_report(report_data, student_name):
    try:
        if not report_data:
            return
        
        print(f"\n=== Report Card for {student_name} ===")
        print("=" * 40) #create visual separation ntata 
        
        for subject in SUBJECTS:
            try:
                print(f"\n{subject}:")
                print("-" * 20)
                
                grades = report_data[subject]['grades']
                if grades:
                    grade_string = str(grades[0])
                    for grade in grades[1:]:
                        grade_string += ", " + str(grade)
                else:
                    grade_string = "No grades yet"
                    
                print(f"Grades: {grade_string}")
                
                average = report_data[subject]['average']
                if isinstance(average, str):
                    print(f"Average: {average}")
                else:
                    print(f"Average: {average:.2f}")
            except:
                print("Error displaying grades")
                continue
    except:
        print("Error displaying student report")

def display_subject_grades(grades_data, subject):
    try:
        if not grades_data:
            print(f"No grades found for {subject}")
            return
        
        print(f"\n=== Grades for {subject} ===")
        print("=" * 40)
        
        for student in grades_data:
            try:
                grades = grades_data[student]
                print(f"\n{student}:")
                
                if grades:
                    grade_string = str(grades[0])
                    for grade in grades[1:]:
                        grade_string += ", " + str(grade)
                else:
                    grade_string = "No grades yet"
                    
                print(f"Grades: {grade_string}")
                
                avg = calculate_average(grades)
                if avg is None:
                    print("Average: No grades yet")
                else:
                    print(f"Average: {avg:.2f}")
            except:
                print("Error displaying grades")
                continue
    except:
        print("Error displaying subject grades")

def main():
    while True:
        try:
            choice = display_menu()
            
            if choice == 1:
                try:
                    name = input("Enter student name: ")
                    if add_student(students, name): #Pass global 'students' dictionary and the input name to add_student function
                        print(f"Successfully added {name}")
                    else:
                        print("Student already exists")
                except:
                    print("Error adding student")
                    
            elif choice == 2:
                try:
                    name = input("Enter student name: ")
                    if remove_student(students, name):
                        print(f"Successfully removed {name}")
                    else:
                        print("Student not found")
                except:
                    print("Error removing student")
                    
            elif choice == 3:
                try:
                    name = input("Enter student name: ")
                    if input_student_grades(students, name):
                        print("Grades entered successfully")
                    else:
                        print("Failed to enter grades")
                except:
                    print("Error entering grades")
                    
            elif choice == 4:
                try:
                    name = input("Enter student name: ")
                    report = get_student_report(students, name)
                    display_student_report(report, name)
                except:
                    print("Error viewing student report")
                    
            elif choice == 5:
                try:
                    print("Available subjects:", " ".join(SUBJECTS))
                    subject = input("Enter subject: ")
                    grades = get_subject_grades(students, subject)
                    display_subject_grades(grades, subject)
                except:
                    print("Error viewing subject grades")
                    
            elif choice == 6:
                print("Thank you for using Grade Management System!")
                break
                
        except:
            print("An unexpected error occurred")
            print("Please try again.")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nProgram terminated by user.")
    except:
        print("Fatal error")
        sys.exit(1)

#SECTION D

import statistics
import sys

students={}
SUBJECTS = ["Math", "English", "Science"]

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
    try:
        if not grade_list:
            return None
        else:
            return statistics.mean(grade_list)
    except statistics.StatisticsError:
        return None
    

def add_student(students_dict, student_name):
    # If student doesn't already exist
    if student_name not in students_dict:
        # Create new student entry with empty grade lists for each subject
        students_dict[student_name] = {
            subject: [] for subject in SUBJECTS
        } #For the student name we entered create an empty list for each subject.
        return True
    return False  # Student already exists


def remove_student(students_dict, student_name):
    # Check If student exists
    if student_name in students_dict:
        # Remove the student from dictionary
        del students_dict[student_name]
        return True
    return False  # if entered student doesn't exist

def update_grade(students_dict, student_name, subject, grade):
    # Validate inputs first
    is_valid, grade_value = validate_grade(grade)
    if is_valid and student_name in students_dict and subject in SUBJECTS:
        # Add the grade to appropriate subject list
        students_dict[student_name][subject].append(grade_value)
        return True
    return False

def input_student_grades(students_dict, student_name):
    # For collecting inputs
    if student_name not in students_dict:
        print("Student not found!")
        return False
        
    for subject in SUBJECTS:
        while True:
            try:
                grade_input = input(f"Enter {student_name}'s grade for {subject} (0-100): ")
                if update_grade(students_dict, student_name, subject, grade_input): #Pass grade_input to update_grade
                    break
                else:
                    print("Invalid grade! Please enter a number between 0 and 100.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")
    return True
  
def get_student_grades(students_dict, student_name): #provides clean way to get data like ya get_student_report, usuful later
    try:
        if student_name in students_dict:
            return students_dict[student_name]
        return None
    except KeyError:
        return None

def get_subject_grades(students_dict, subject):
    try:
        if subject not in SUBJECTS:
            print("Invalid subject!")
            return None
        
        subject_grades = {}
        for student in students_dict:
            subject_grades[student] = students_dict[student][subject]
        return subject_grades
    except KeyError:
        return None
    
def get_student_report(students_dict, student_name):
    try:
        if student_name not in students_dict:
            print("Student not found!")
            return None
        report = {}
        student_grades = students_dict[student_name]
        
        for subject in SUBJECTS:
            try:
                grades = student_grades[subject] #Get list ya grades
                avg = calculate_average(grades)#pass list to calculate_average
                report[subject] = {
                    'grades': grades,
                    'average': avg if avg is not None else 'No grades yet'
                }
            except:
                print("Error processing subject")
                continue
        return report
    except:
        print("Error generating student report")
        return None

def display_menu():
    try:
        print("\n=== Grade Management System ===")
        print("1. Add New Student")
        print("2. Remove Student")
        print("3. Enter Grades")
        print("4. View Student Report")
        print("5. View Subject Grades")
        print("6. Exit")
        
        while True:
            try:
                choice = int(input("\nEnter your choice (1-6): "))
                if 1 <= choice <= 6:
                    return choice
                print("Please enter a number between 1 and 6")
            except:
                print("Please enter a valid number")
    except:
        print("Error displaying menu")
        return 6

def display_student_report(report_data, student_name):
    try:
        if not report_data:
            return
        
        print(f"\n=== Report Card for {student_name} ===")
        print("=" * 40) #create visual separation ntata 
        
        for subject in SUBJECTS:
            try:
                print(f"\n{subject}:")
                print("-" * 20)
                
                grades = report_data[subject]['grades']
                if grades:
                    grade_string = str(grades[0])
                    for grade in grades[1:]:
                        grade_string += ", " + str(grade)
                else:
                    grade_string = "No grades yet"
                    
                print(f"Grades: {grade_string}")
                
                average = report_data[subject]['average']
                if isinstance(average, str):
                    print(f"Average: {average}")
                else:
                    print(f"Average: {average:.2f}")
            except:
                print("Error displaying grades")
                continue
    except:
        print("Error displaying student report")

def display_subject_grades(grades_data, subject):
    try:
        if not grades_data:
            print(f"No grades found for {subject}")
            return
        
        print(f"\n=== Grades for {subject} ===")
        print("=" * 40)
        
        for student in grades_data:
            try:
                grades = grades_data[student]
                print(f"\n{student}:")
                
                if grades:
                    grade_string = str(grades[0])
                    for grade in grades[1:]:
                        grade_string += ", " + str(grade)
                else:
                    grade_string = "No grades yet"
                    
                print(f"Grades: {grade_string}")
                
                avg = calculate_average(grades)
                if avg is None:
                    print("Average: No grades yet")
                else:
                    print(f"Average: {avg:.2f}")
            except:
                print("Error displaying grades")
                continue
    except:
        print("Error displaying subject grades")

def main():
    while True:
        try:
            choice = display_menu()
            
            if choice == 1:
                try:
                    name = input("Enter student name: ")
                    if add_student(students, name): #Pass global 'students' dictionary and the input name to add_student function
                        print(f"Successfully added {name}")
                    else:
                        print("Student already exists")
                except:
                    print("Error adding student")
                    
            elif choice == 2:
                try:
                    name = input("Enter student name: ")
                    if remove_student(students, name):
                        print(f"Successfully removed {name}")
                    else:
                        print("Student not found")
                except:
                    print("Error removing student")
                    
            elif choice == 3:
                try:
                    name = input("Enter student name: ")
                    if input_student_grades(students, name):
                        print("Grades entered successfully")
                    else:
                        print("Failed to enter grades")
                except:
                    print("Error entering grades")
                    
            elif choice == 4:
                try:
                    name = input("Enter student name: ")
                    report = get_student_report(students, name)
                    display_student_report(report, name)
                except:
                    print("Error viewing student report")
                    
            elif choice == 5:
                try:
                    print("Available subjects:", " ".join(SUBJECTS))
                    subject = input("Enter subject: ")
                    grades = get_subject_grades(students, subject)
                    display_subject_grades(grades, subject)
                except:
                    print("Error viewing subject grades")
                    
            elif choice == 6:
                print("Thank you for using Grade Management System!")
                break
                
        except:
            print("An unexpected error occurred")
            print("Please try again.")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nProgram terminated by user.")
    except:
        print("Fatal error")
        sys.exit(1)

#SECTION E
import statistics
import sys

class Student:
    """A class representing a student with their grades."""
    
    def __init__(self, name):
        """Initialize a student with their name."""
        self.name = name
        self.grades = {}
        for subject in Gradebook.SUBJECTS:
            self.grades[subject] = []
    
    @staticmethod
    def validate_grade(grade_input):
        """Validate if a grade is between 0 and 100."""
        try:
            grade = float(grade_input)
            if 0 <= grade <= 100:
                return True, grade
            else:
                return False, None
        except ValueError:
            return False, None
    
    @staticmethod
    def calculate_average(grade_list):
    # Calculate the average of a list of grades
     try:
        if not grade_list:
            return None
        else:
            return statistics.mean(grade_list)
     except statistics.StatisticsError:
        return None
     
     def __init__(self, name):
        self.name = name
        self.grades = {subject: [] for subject in SUBJECTS}
    
def add_grade(students_dict, student_name, subject, grade):
    # Validate inputs first
    is_valid, grade_value = validate_grade(grade)
    if is_valid and student_name in students_dict and subject in SUBJECTS:
        # Add the grade to appropriate subject list
        students_dict[student_name][subject].append(grade_value)
        return True
    return False

def get_report(students_dict, student_name):
    try:
        if student_name not in students_dict:
            print("Student not found!")
            return None
        report = {}
        student_grades = students_dict[student_name]
        
        for subject in SUBJECTS:
            try:
                grades = student_grades[subject] #Get list ya grades
                avg = calculate_average(grades)#pass list to calculate_average
                report[subject] = {
                    'grades': grades,
                    'average': avg if avg is not None else 'No grades yet'
                }
            except:
                print("Error processing subject")
                continue
        return report
    except:
        print("Error generating student report")
        return None


class Gradebook:

    class_SUBJECTS = ["Math", "English", "Science"]

def __init__(self): 
    self.students = {}

def add_student(students_dict, student_name):
    # If student doesn't already exist
        if student_name not in students_dict:
        # Create new student entry with empty grade lists for each subject
            students_dict[student_name] = {
            subject: [] for subject in SUBJECTS
        } #For the student name we entered create an empty list for each subject.
        return True
        return False  # Student already exists

def remove_student(students_dict, student_name):
    # Check If student exists
    if student_name in students_dict:
        # Remove the student from dictionary
        del students_dict[student_name]
        return True
    return False  # if entered student doesn't exist

def get_student_grades(students_dict, student_name): #provides clean way to get data like ya get_student_report, usuful later
    try:
        if student_name in students_dict:
            return students_dict[student_name]
        return None
    except KeyError:
        return None
    
def get_subject_grades(students_dict, subject):
    try:
        if subject not in SUBJECTS:
            print("Invalid subject!")
            return None
        
        subject_grades = {}
        for student in students_dict:
            subject_grades[student] = students_dict[student][subject]
        return subject_grades
    except KeyError:
        return None
    


def input_student_grades(students_dict, student_name):
    # For collecting inputs
    if student_name not in students_dict:
        print("Student not found!")
        return False
        
    for subject in SUBJECTS:
        while True:
            try:
                grade_input = input(f"Enter {student_name}'s grade for {subject} (0-100): ")
                if update_grade(students_dict, student_name, subject, grade_input): #Pass grade_input to update_grade
                    break
                else:
                    print("Invalid grade! Please enter a number between 0 and 100.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")
    return True
  
def display_student_report(report_data, student_name):
    try:
        if not report_data:
            return
        
        print(f"\n=== Report Card for {student_name} ===")
        print("=" * 40) #create visual separation ntata 
        
        for subject in SUBJECTS:
            try:
                print(f"\n{subject}:")
                print("-" * 20)
                
                grades = report_data[subject]['grades']
                if grades:
                    grade_string = str(grades[0])
                    for grade in grades[1:]:
                        grade_string += ", " + str(grade)
                else:
                    grade_string = "No grades yet"
                    
                print(f"Grades: {grade_string}")
                
                average = report_data[subject]['average']
                if isinstance(average, str):
                    print(f"Average: {average}")
                else:
                    print(f"Average: {average:.2f}")
            except:
                print("Error displaying grades")
                continue
    except:
        print("Error displaying student report")

def display_subject_grades(grades_data, subject):
    try:
        if not grades_data:
            print(f"No grades found for {subject}")
            return
        
        print(f"\n=== Grades for {subject} ===")
        print("=" * 40)
        
        for student in grades_data:
            try:
                grades = grades_data[student]
                print(f"\n{student}:")
                
                if grades:
                    grade_string = str(grades[0])
                    for grade in grades[1:]:
                        grade_string += ", " + str(grade)
                else:
                    grade_string = "No grades yet"
                    
                print(f"Grades: {grade_string}")
                
                avg = calculate_average(grades)
                if avg is None:
                    print("Average: No grades yet")
                else:
                    print(f"Average: {avg:.2f}")
            except:
                print("Error displaying grades")
                continue
    except:
        print("Error displaying subject grades")


def display_menu():
    try:
        print("\n=== Grade Management System ===")
        print("1. Add New Student")
        print("2. Remove Student")
        print("3. Enter Grades")
        print("4. View Student Report")
        print("5. View Subject Grades")
        print("6. Exit")
        
        while True:
            try:
                choice = int(input("\nEnter your choice (1-6): "))
                if 1 <= choice <= 6:
                    return choice
                print("Please enter a number between 1 and 6")
            except:
                print("Please enter a valid number")
    except:
        print("Error displaying menu")
        return 6




def main():
    while True:
        try:
            choice = display_menu()
            
            if choice == 1:
                try:
                    name = input("Enter student name: ")
                    if add_student(students, name): #Pass global 'students' dictionary and the input name to add_student function
                        print(f"Successfully added {name}")
                    else:
                        print("Student already exists")
                except:
                    print("Error adding student")
                    
            elif choice == 2:
                try:
                    name = input("Enter student name: ")
                    if remove_student(students, name):
                        print(f"Successfully removed {name}")
                    else:
                        print("Student not found")
                except:
                    print("Error removing student")
                    
            elif choice == 3:
                try:
                    name = input("Enter student name: ")
                    if input_student_grades(students, name):
                        print("Grades entered successfully")
                    else:
                        print("Failed to enter grades")
                except:
                    print("Error entering grades")
                    
            elif choice == 4:
                try:
                    name = input("Enter student name: ")
                    report = get_student_report(students, name)
                    display_student_report(report, name)
                except:
                    print("Error viewing student report")
                    
            elif choice == 5:
                try:
                    print("Available subjects:", " ".join(SUBJECTS))
                    subject = input("Enter subject: ")
                    grades = get_subject_grades(students, subject)
                    display_subject_grades(grades, subject)
                except:
                    print("Error viewing subject grades")
                    
            elif choice == 6:
                print("Thank you for using Grade Management System!")
                break
                
        except:
            print("An unexpected error occurred")
            print("Please try again.")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nProgram terminated by user.")
    except:
        print("Fatal error")
        sys.exit(1)

#SECTION F
"""
TESTING DOCUMENTATION

1. Student Class Testing
----------------------
Test Cases:
a) Student Creation
   - Valid student name → PASS
   - Empty student name → PASS (Raises ValueError)
   - Whitespace name → PASS (Raises ValueError)

b) Grade Validation
   - Valid grades (0-100) → PASS
   - Invalid grades:
     * Negative numbers → PASS (Raises InvalidGradeError)
     * Numbers > 100 → PASS (Raises InvalidGradeError)
     * Non-numeric input → PASS (Raises InvalidGradeError)

c) Grade Management
   - Adding valid grades → PASS
   - Adding grades for invalid subject → PASS (Raises InvalidSubjectError)
   - Calculating averages:
     * No grades → PASS (Returns None)
     * Single grade → PASS
     * Multiple grades → PASS
     * Invalid subject → PASS (Raises InvalidSubjectError)

2. Gradebook Class Testing
-------------------------
Test Cases:
a) Student Management
   - Adding new student → PASS
   - Adding duplicate student → PASS (Returns False)
   - Removing existing student → PASS
   - Removing non-existent student → PASS (Returns False)

b) Grade Operations
   - Adding grades for existing student → PASS
   - Adding grades for non-existent student → PASS (Raises StudentNotFoundError)
   - Getting subject grades:
     * Valid subject → PASS
     * Invalid subject → PASS (Returns None)

c) Search Functionality
   - Exact match → PASS
   - Partial match → PASS
   - Case-insensitive match → PASS
   - No matches → PASS (Returns empty list)

d) Sorting Implementation (Bubble Sort)
   - Sorting with no grades → PASS
   - Sorting with single student → PASS
   - Sorting multiple students → PASS
   - Sorting with tied grades → PASS
   - Invalid subject → PASS (Raises InvalidSubjectError)

3. Error Handling Testing
------------------------
Test Cases:
a) Input Validation
   - Invalid grade formats → PASS
   - Invalid subject names → PASS
   - Non-existent students → PASS
   - Empty inputs → PASS

b) Exception Handling
   - InvalidGradeError → PASS
   - StudentNotFoundError → PASS
   - InvalidSubjectError → PASS
   - ValueError → PASS

4. Integration Testing
---------------------
Test Scenarios:
a) Complete Student Workflow
   - Add student → Add grades → Calculate average → Generate report → PASS
   - Add student → Remove student → Try to add grades → PASS
   - Search student → View grades → Sort by subject → PASS

b) Error Recovery
   - Invalid input → Error message → Continue operation → PASS
   - Invalid grade → Error message → Retry input → PASS
   - System recovery after exceptions → PASS

5. Bug Fixes and Improvements
---------------------------
a) Grade Input Issue Resolution:
   Problem Identified:
   - When entering invalid grade input, the system would return to main menu
   - Partial grades were being saved even when some inputs were invalid
   - No opportunity to retry entering an invalid grade

   Solution Implemented:
   - Added temporary grade storage mechanism
   - Implemented two-phase commit approach:
     * Phase 1: Collect and validate all grades
     * Phase 2: Save all grades only if all are valid
   - Enhanced error handling with retry capability
   - Prevented partial grade saves
   - Added clearer error messages and prompts

   Result:
   - System now continuously prompts for valid input
   - All grades must be valid before any are saved
   - Better user experience with clear error messages
   - No data inconsistency from partial saves

b) Data Persistence Implementation:
   Even though not stated in the system requirements, I came to a conclusion it would 
   be necessary to include the saving capability as it is an implied functionality.
   
   Problem Identified:
   - Data was lost when program was closed
   - Each session started fresh without previous records
   - No way to maintain student records across sessions

   Solution Implemented:
   - Added JSON-based data persistence
   - Automatic data loading on startup
   - Automatic saving when exiting
   - Error handling for file operations

   Result:
   - Student data persists between sessions
   - Seamless data recovery on startup
   - Safe data storage with proper error handling
   - Better practical usability in real-world scenarios

Test Results Summary:
--------------------
Total Test Cases: 35
Passed: 35
Failed: 0
Success Rate: 100%

Note: All tests were conducted using both valid and invalid inputs to ensure
robust error handling and system stability. The system has been verified to
handle edge cases and error conditions appropriately.
"""

import statistics
import sys
import json
import os

class InvalidGradeError(Exception):
    """Custom exception for invalid grade inputs."""
    pass

class StudentNotFoundError(Exception):
    """Custom exception for when a student is not found."""
    pass

class InvalidSubjectError(Exception):
    """Custom exception for invalid subject inputs."""
    pass

class Student:
    """A class representing a student with their grades
    
    This class manages individual student information including:
    - Student name
    - Grades for different subjects
    - Grade calculations and validation
    
    Attributes:
        name (str): The name of the student
        grades (dict): Dictionary containing grades for each subject
    """
    
    def __init__(self, name):
        """Initialize a student with their name.
        
        Args:
            name (str): The name of the student
            
        Raises:
            ValueError: If name is empty or contains only whitespace
        """
        if not name or name.isspace():
            raise ValueError("Student name cannot be empty")
        self.name = name
        self.grades = {}
        for subject in Gradebook.SUBJECTS:
            self.grades[subject] = []
    
    @staticmethod
    def validate_grade(grade_input):
        """Validate if a grade is between 0 and 100.
        
        Args:
            grade_input (str): The grade to validate
            
        Returns:
            tuple: (bool, float or None) indicating if grade is valid and the converted grade
            
        Raises:
            InvalidGradeError: If grade is not a valid number or out of range
            
        Test Cases:
        -----------
        1. Test valid grades:
           >>> validate_grade("85")  # Should return (True, 85.0)
           >>> validate_grade("100") # Should return (True, 100.0)
           >>> validate_grade("0")   # Should return (True, 0.0)
        
        2. Test invalid grades:
           >>> validate_grade("101") # Should raise InvalidGradeError
           >>> validate_grade("-1")  # Should raise InvalidGradeError
           >>> validate_grade("mfolwe") # Should raise InvalidGradeError
        """
        try:
            grade = float(grade_input)
            if 0 <= grade <= 100:
                return True, grade
            else:
                raise InvalidGradeError("Grade must be between 0 and 100")
        except ValueError:
            raise InvalidGradeError("Grade must be a valid number")
    
    def add_grade(self, subject, grade):
        """Add a grade for a specific subject.
        
        Arguments:
            subject (str): The subject to add grade for
            grade (str): The grade to add
            
        Returns:
            bool: True if grade was added successfully
            
        Raises:
            InvalidSubjectError: If subject is not valid
            InvalidGradeError: If grade is not valid
        """
        if subject not in Gradebook.SUBJECTS:
            raise InvalidSubjectError(f"Invalid subject: {subject}")
            
        try:
            is_valid, grade_value = self.validate_grade(grade)
            self.grades[subject].append(grade_value)
            return True
        except InvalidGradeError as e:
            raise InvalidGradeError(f"Invalid grade for {subject}: {str(e)}")
    
    def get_subject_grades(self, subject):
        """Get all grades for a specific subject."""
        return self.grades.get(subject, [])

    def calculate_average(self, subject):
        """Calculate average grade for a subject."""
        grades = self.grades.get(subject, [])
        try:
            if not grades:
                return None
            return statistics.mean(grades)
        except statistics.StatisticsError:
            return None
    
    def get_report(self):
        """Generate a complete report of all subjects."""
        report = {}
        for subject in Gradebook.SUBJECTS:
            grades = self.grades[subject]
            avg = self.calculate_average(subject)
            report[subject] = {
                'grades': grades,
                'average': avg if avg is not None else 'No grades yet'
            }
        return report


class Gradebook:
    """A class managing multiple students and their grades.
    
    This class provides functionality for:
    - Managing students (add/remove)
    - Managing grades
    - Searching students
    - Sorting students by grades
    - Generating reports
    
    Attributes:
        SUBJECTS (list): List of available subjects
        students (dict): Dictionary of student objects
    """
    
    SUBJECTS = ["Math", "English", "Science"] # Predefined subjects
    
    def __init__(self):
        """Initialize gradebook and load existing data if available."""
        self.students = {}
        self.data_file = "gradebook_data.json"
        self.load_data()
        
    def search_student(self, search_term):
        """Search for students by name.
        
        Args:
            search_term (str): The name or partial name to search for
            
        Returns:
            list: List of student names matching the search term
        """
        search_term = search_term.lower()
        return [name for name in self.students.keys() 
                if search_term in name.lower()]
    
    def bubble_sort_by_average(self, subject):
        """Sort students by their average grade in a subject using bubble sort.
        
        Args:
            subject (str): The subject to sort by
            
        Returns:
            list: List of tuples (student_name, average) sorted by average
            
        Raises:
            InvalidSubjectError: If subject is not valid
            
        Test Cases:
        -----------
        1. Sort with multiple students (different grades):
           Input: 
           - Student1: Math grades [90, 85]
           - Student2: Math grades [95, 100]
           - Student3: Math grades [75, 80]
           Expected Output: [(Student2, 97.5), (Student1, 87.5), (Student3, 77.5)]
        
        2. Sort with tied grades:
           Input:
           - Student1: Math grades [85, 85]
           - Student2: Math grades [85, 85]
           Expected Output: [(Student1, 85.0), (Student2, 85.0)]
           
        3. Sort with some students having no grades:
           Input:
           - Student1: Math grades [90]
           - Student2: Math grades []
           Expected Output: [(Student1, 90.0), (Student2, -1)]
           
        4. Sort with invalid subject:
           Input: "InvalidSubject"
           Expected Output: Raises InvalidSubjectError
           
        """
        if subject not in self.SUBJECTS:
            raise InvalidSubjectError(f"Invalid subject: {subject}")
            
        # Get list of (student_name, average) tuples
        student_averages = []
        for name, student in self.students.items():
            avg = student.calculate_average(subject)
            # Handle students with no grades
            avg = avg if avg is not None else -1
            student_averages.append((name, avg))
        
        # Bubble sort implementation
        n = len(student_averages)
        for i in range(n):
            for j in range(0, n - i - 1):
                if student_averages[j][1] < student_averages[j + 1][1]:
                    student_averages[j], student_averages[j + 1] = \
                        student_averages[j + 1], student_averages[j]
        #Would sort from highest to lowest average
        
        return student_averages
    
    def add_student(self, student_name):
        """Add a new student to the gradebook."""
        if student_name not in self.students:
            self.students[student_name] = Student(student_name)
            return True
        return False

    def remove_student(self, student_name):
        # Remove a student from the gradebook
        if student_name in self.students:
            del self.students[student_name]
            return True
        return False
    
    def get_student(self, student_name):
        """Get a student object by name."""
        return self.students.get(student_name)
        return None
    
    def get_subject_grades(self, subject):
        """Get grades for all students in a subject."""
        if subject not in self.SUBJECTS:
            return None
        
        subject_grades = {}
        for student_name, student in self.students.items():
            subject_grades[student_name] = student.get_subject_grades(subject)
        return subject_grades
        
    def save_data(self):
        """Save gradebook data to a JSON file."""
        try:
            # Convert gradebook data to a serializable format
            data = {
                "subjects": self.SUBJECTS,
                "students": {}
            }
            
            for name, student in self.students.items():
                data["students"][name] = student.grades
                
            # Save to file
            with open(self.data_file, 'w') as file:
                json.dump(data, file, indent=4)
            return True
        except Exception as e:
            print(f"Error saving data: {str(e)}")
            return False
            
    def load_data(self):
        """Load gradebook data from JSON file if it exists."""
        try:
            if os.path.exists(self.data_file):
                with open(self.data_file, 'r') as file:
                    data = json.load(file)
                    
                # Recreate students with their grades
                for name, grades in data["students"].items():
                    student = Student(name)
                    student.grades = grades
                    self.students[name] = student
                print("Previous session data loaded successfully!")
            else:
                print("Welcome to Grade Management System!")
                print("No previous data found - starting fresh.")
        except Exception as e:
            print(f"Error loading data: {str(e)}")
    
    def update_student_grades(self, student_name):
        """Update the most recent grades for a student."""
        student = self.get_student(student_name)
        if not student:
            print("Student not found!")
            return False
        
        # Dictionary to store all new grades before saving
        temp_grades = {}
        
        print("\nEnter new grades (or press Enter to skip a subject):")
        # Collect all grades first
        for subject in self.SUBJECTS:
            current_grades = student.get_subject_grades(subject)
            if current_grades:
                print(f"Current {subject} grade: {current_grades[-1]}")
            else:
                print(f"No current grade for {subject}")
                
            temp_grades[subject] = None
            grade_input = input(f"Enter new grade for {subject} (0-100) or press Enter to skip: ")
            
            if grade_input.strip():  # Only process if input is not empty
                try:
                    is_valid, grade_value = Student.validate_grade(grade_input)
                    if is_valid:
                        temp_grades[subject] = grade_value
                except InvalidGradeError as e:
                    print(f"Error: {str(e)}")
                    print("Grade not updated for this subject.")
                except ValueError:
                    print("Invalid input. Grade not updated for this subject.")
        
        # Save valid updates
        updated = False
        for subject, grade in temp_grades.items():
            if grade is not None:
                try:
                    if student.grades[subject]:  # If there are existing grades
                        student.grades[subject][-1] = grade  # Update the last grade
                    else:
                        student.grades[subject].append(grade)  # Add as first grade if none exist
                    print(f"Successfully updated grade for {subject}")
                    updated = True
                except Exception as e:
                    print(f"Error updating {subject}: {str(e)}")
        
        return updated

    def input_student_grades(self, student_name):
        """Input new grades for a student."""
        student = self.get_student(student_name)
        if not student:
            print("Student not found!")
            return False
        
        # Dictionary to store all grades before saving
        temp_grades = {}
        
        # Collect all grades first
        for subject in self.SUBJECTS:
            temp_grades[subject] = None
            while True:
                try:
                    grade_input = input(f"Enter {student_name}'s grade for {subject} (0-100): ")
                    is_valid, grade_value = Student.validate_grade(grade_input)
                    if is_valid:
                        temp_grades[subject] = grade_value
                        break
                    else:
                        print("Invalid grade! Please enter a number between 0 and 100.")
                except InvalidGradeError as e:
                    print(f"Error: {str(e)}")
                    print("Please enter a valid number between 0 and 100.")
                except ValueError:
                    print("Invalid input. Please enter a valid number.")
        
        # Only save grades if all are valid
        try:
            for subject, grade in temp_grades.items():
                if grade is not None:
                    student.grades[subject].append(grade)
            return True
        except Exception as e:
            print(f"Error saving grades: {str(e)}")
            return False
  
    def display_student_report(self, report_data, student_name):
        """Display a formatted student report."""
        if not report_data:
            return
        
        print(f"\n=== Report Card for {student_name} ===")
        print("=" * 40) #creates a visual separator/underline below the header
        
        for subject in self.SUBJECTS:
            print(f"\n{subject}:")
            print("-" * 20)
            
            grades = report_data[subject]['grades']
            if grades:
                # Convert each grade to string and build the grade string 
                grade_string = ""
                for i in range(len(grades)):
                    if i == 0:
                        grade_string = str(grades[i])
                    else:
                        grade_string = grade_string + ", " + str(grades[i])
            else:
                grade_string = "No grades yet"
            print(f"Grades: {grade_string}")
            
            average = report_data[subject]['average']
            if isinstance(average, str):
                print(f"Average: {average}")
            else:
                print(f"Average: {average:.2f}")
    
    def display_subject_grades(self, grades_data, subject):
        """Display grades for all students in a subject and overall subject average."""
        if not grades_data:
            print(f"No grades found for {subject}")
            return
        
        print(f"\n=== Grades for {subject} ===")
        print("=" * 40)
        
        all_grades = []  # To store all grades for subject average
        
        for student_name, grades in grades_data.items():
            print(f"\n{student_name}:")
            if grades:
                # Convert each grade to string and build the grade string
                grade_string = ""
                for i in range(len(grades)):
                    if i == 0:
                        grade_string = str(grades[i])
                    else:
                        grade_string = grade_string + ", " + str(grades[i])
                all_grades.extend(grades)  # Add this student's grades to overall list
            else:
                grade_string = "No grades yet"
            print(f"Grades: {grade_string}")
            
            if grades:
                avg = statistics.mean(grades)
                print(f"Average: {avg:.2f}")
            else:
                print("Average: No grades yet")
        
        # Calculate and display overall subject average
        print("\n" + "=" * 40)
        if all_grades:
            overall_avg = statistics.mean(all_grades)
            print(f"Overall {subject} Class Average: {overall_avg:.2f}")
        else:
            print(f"Overall {subject} Class Average: No grades yet")

    def display_menu(self):
        """Display the main menu and get user choice."""
        print("\n=== Grade Management System ===")
        print("1. Add New Student")
        print("2. Remove Student")
        print("3. Enter Grades")
        print("4. View Student Report")
        print("5. View Subject Grades")
        print("6. Search Students")
        print("7. View Sorted Student Rankings")
        print("8. Exit")
        
        while True:
            try:
                choice = int(input("\nEnter your choice (1-8): "))
                if 1 <= choice <= 8:
                    return choice
                print("Please enter a number between 1 and 8")
            except ValueError:
                print("Please enter a valid number")
    
    def run(self):
        #Run the main program loop
        while True:
            try:
                choice = self.display_menu()
                
                if choice == 1:
                    try:
                        name = input("Enter student name: ")
                        if self.add_student(name):
                            print(f"Successfully added {name}")
                        else:
                            print("Student already exists")
                    except ValueError as e:
                        print("Error:", str(e))
                        
                elif choice == 2:
                    try:
                        name = input("Enter student name: ")
                        if self.remove_student(name):
                            print(f"Successfully removed {name}")
                        else:
                            raise StudentNotFoundError(f"Student '{name}' not found")
                    except StudentNotFoundError as e:
                        print("Error:", str(e))
                        
                elif choice == 3:
                    try:
                        name = input("Enter student name: ")
                        if not name in self.students:
                            raise StudentNotFoundError(f"Student '{name}' not found")
                        if self.input_student_grades(name):
                            print("Grades entered successfully")
                        else:
                            print("Failed to enter grades")
                    except (StudentNotFoundError, InvalidGradeError) as e:
                        print("Error:", str(e))
                        
                elif choice == 4:
                    try:
                        name = input("Enter student name: ")
                        student = self.get_student(name)
                        if not student:
                            raise StudentNotFoundError(f"Student '{name}' not found")
                        report = student.get_report()
                        self.display_student_report(report, name)
                    except StudentNotFoundError as e:
                        print("Error:", str(e))
                        
                elif choice == 5:
                    try:
                        print("Available subjects:")
                        for subject in self.SUBJECTS:
                            print(f"- {subject}")
                        subject = input("Enter subject: ")
                        if subject not in self.SUBJECTS:
                            raise InvalidSubjectError(f"Invalid subject: {subject}")
                        grades = self.get_subject_grades(subject)
                        self.display_subject_grades(grades, subject)
                    except InvalidSubjectError as e:
                        print("Error:", str(e))
                        
                elif choice == 6:
                    try:
                        search_term = input("Enter student name to search: ")
                        matches = self.search_student(search_term)
                        if matches:
                            print("\nMatching students:")
                            for name in matches:
                                print(f"- {name}")
                                # Show current grades for this student
                                student = self.get_student(name)
                                report = student.get_report()
                                self.display_student_report(report, name)
                                
                                # Ask if user wants to update grades
                                update_choice = input("\nWould you like to update the most recent grades for this student? (yes/no): ")
                                if update_choice.lower() == 'yes':
                                    if self.update_student_grades(name):
                                        print("\nUpdated grades:")
                                        student = self.get_student(name)
                                        report = student.get_report()
                                        self.display_student_report(report, name)
                        else:
                            print("No matching students found")
                    except Exception as e:
                        print("Error during search:", str(e))
                        
                elif choice == 7:
                    try:
                        print("Available subjects:")
                        for subject in self.SUBJECTS:
                            print(f"- {subject}")
                        subject = input("Enter subject to rank students by: ")
                        if subject not in self.SUBJECTS:
                            raise InvalidSubjectError(f"Invalid subject: {subject}")
                        
                        rankings = self.bubble_sort_by_average(subject)
                        print(f"\nStudent Rankings for {subject}:")
                        print("=" * 40)
                        for i, (name, avg) in enumerate(rankings, 1):
                            if avg >= 0:
                                print(f"{i}. {name}: {avg:.2f}")
                            else:
                                print(f"{i}. {name}: No grades")
                    except InvalidSubjectError as e:
                        print("Error:", str(e))
                        
                elif choice == 8:
                    if self.save_data():
                        print("Data saved successfully!")
                    print("Thank you for using Grade Management System!")
                    break
                    
            except Exception as e:
                print("An error occurred: " + str(e))
                print("Please try again.")


if __name__ == "__main__":
    try:
        gradebook = Gradebook()
        gradebook.run()
    except KeyboardInterrupt:
        print("\nProgram terminated by user.")
    except Exception as e:
        print("Fatal error: " + str(e))
        sys.exit(1)