from database.setup import create_tables
from helpers import (
    list_students, list_courses, list_instructors, list_enrollments,
    add_student, add_course, add_instructor, enroll_student
)

def main():
    create_tables()
    while True:
        print("""
        1. List students
        2. List courses
        3. List instructors
        4. List enrollments
        5. Add student
        6. Add course
        7. Add instructor
        8. Enroll student
        9. Exit
        """)
        choice = input("Enter your choice:")
        if choice == '1':
            list_students()
        elif choice == '2':
            list_courses()
        elif choice == '3':
            list_instructors()
        elif choice == '4':
            list_enrollments()
        elif choice == '5':
            add_student()
        elif choice == '6':
            add_course()
        elif choice == '7':
            add_instructor()
        elif choice == '8':
            enroll_student()
        elif choice == '9':
            print("Goodbye, thanks for using enrollment manager!")
            break
        else:
            print("Invalid choice")
            

if __name__ == "__main__":
    main()