from database.setup import create_tables
from helpers import (
    list_students, list_courses, list_instructors, list_enrollments,
    add_student, add_course, add_instructor, enroll_student,
    update_student, update_course, update_instructor, update_enrollment,
    delete_student, delete_course, delete_instructor, delete_enrollment
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
        9. Update student
        10. Update course
        11. Update instructor
        12. Update enrollment
        13. Delete student
        14. Delete course
        15. Delete instructor
        16. Delete enrollment
        17. Clear database
        18. Exit
        """)
        choice = input("Enter your choice: ")
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
            update_student()
        elif choice == '10':
            update_course()
        elif choice == '11':
            update_instructor()
        elif choice == '12':
            update_enrollment()
        elif choice == '13':
            delete_student()
        elif choice == '14':
            delete_course()
        elif choice == '15':
            delete_instructor()
        elif choice == '16':
            delete_enrollment()
        elif choice == '17':
            clear_database()
            print("Database cleared.")
        elif choice == '18':
            print("Goodbye, thanks for using us!")
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
