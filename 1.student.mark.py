def input_number_of_students():
    return int(input("Enter the number of students in the class: "))

def input_student_information():
    print("")
    student_id = input("Enter student id: ")
    student_name = input("Enter student name: ")
    student_dob = input("Enter student date of birth: ")
    return student_id, student_name, student_dob

def input_number_of_courses():
    return int(input("Enter number of courses: "))

def input_course_information():
    print("")
    course_id = input("Enter course ID: ")
    course_name = input("Enter course name: ")
    return course_id, course_name

def select_course(courses):
    print("")
    print("Courses List:")
    for i, course in enumerate(courses):
        print(f"{i + 1}, {course[1]}")
    course_i = int(input("Select course number: ")) - 1
    return courses[course_i]

def input_student_marks(students, course_selected):
    marks = {}
    print("")
    print(f"Course selected: {course_selected[1]}")
    print("")
    print("Enter marks for:")
    for student in students:
        mark = float(input(f"Student {student[1]}: "))
        marks[student[1]] = mark
    return marks

def list_courses(courses):
    print("Courses List: ")
    for course in courses:
        print(f" {course[0]} - {course[1]}")
        
def list_students(students):
    print("Student list: ")
    for student in students:
        print(f" {student[0]} - {student[1]}")
        
def show_student_marks(course_selected, marks):
    print(f"Marks for course {course_selected[1]}:")
    for student_name, mark in marks.items():
        print(f" {student_name} {mark}")

   
def display_options():
    print(" _______________________________ ")
    print("|                               |")
    print("|            OPTIONS            |")
    print("|                               |")
    print("| 1, Enter students information |")
    print("| 2, Enter courses information  |")
    print("| 3, Enter marks for student    |")
    print("| 4, Show student list          |")
    print("| 5, Show course list           |")
    print("| 6, Show student marks         |")
    print("| 7, End                        |")
    print("|_______________________________|")
        
## Main

students = []
courses = []

while True:
    display_options()
    choice = int(input("Enter your choice: "))

    if choice == 1:
        num_students = input_number_of_students()
        for _ in range(num_students):
            student = input_student_information()
            students.append(student)
        print("")
        print("Enter students information successfully!")
        print("")
        
    elif choice == 2:
        num_courses = input_number_of_courses()
        for _ in range(num_courses):
            course = input_course_information()
            courses.append(course)
        print("")
        print("Enter courses information successfully!")
        print("")
            
    elif choice == 3:
        course_selected = select_course(courses)
        marks = input_student_marks(students, course_selected)
        print("")
        print("Enter student marks successfully!")
        print("")

    elif choice == 4:
        list_students(students) 
        
    elif choice == 5:
        list_courses(courses)

    elif choice == 6:
        course_selected = select_course(courses)
        show_student_marks(course_selected, marks)
        
    elif choice == 7:
        break
        
    else:
        print("Invalid choice. Please try again!")
    

