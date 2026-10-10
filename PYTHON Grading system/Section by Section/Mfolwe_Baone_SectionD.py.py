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