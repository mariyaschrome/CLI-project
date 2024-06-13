from models.student import Student
from models.course import Course
from models.instructor import Instructor
from models.enrollment import Enrollment

def list_students():
    students = Student.all()
    for student in students:
        print(f"Student ID: {student['id']}, Name: {student['name']}, Age: {student['age']}, Course: {student['course_name']}, Instructor: {student['instructor_name']}")

def list_courses():
    courses = Course.all()
    for course in courses:
        print(f"Course ID: {course['id']}, Name: {course['name']}, Description: {course['description']}")

def list_instructors():
    instructors = Instructor.all()
    for instructor in instructors:
        print(f"Instructor ID: {instructor['id']}, Name: {instructor['name']}, Course ID: {instructor['course_id']}")

def list_enrollments():
    enrollments = Enrollment.all()
    for enrollment in enrollments:
        print(f"Enrollment ID: {enrollment['id']}, Student: {enrollment['student_name']}, Course: {enrollment['course_name']}, Instructor: {enrollment['instructor_name']}")

def add_student():
    name = input("Enter student name: ")
    age = int(input("Enter student age: "))
    course_name = input("Enter course name: ")
    instructor_name = input("Enter instructor name: ")
    student = Student(name, age, course_name, instructor_name)
    student.save()
    print(f"Student {name} added.")

def add_course():
    name = input("Enter course name: ")
    description = input("Enter course description: ")
    course = Course(name, description)
    course.save()
    print(f"Course {name} added.")

def add_instructor():
    name = input("Enter instructor name: ")
    course_id = int(input("Enter course ID: "))
    instructor = Instructor(name, course_id)
    instructor.save()
    print(f"Instructor {name} added.")

def enroll_student():
    student_name = input("Enter student name: ")
    course_name = input("Enter course name: ")
    instructor_name = input("Enter instructor name: ")  
    enrollment = Enrollment(student_name, course_name, instructor_name)  
    enrollment.save()
    print(f"Student {student_name} enrolled in course {course_name} with instructor {instructor_name}")

def update_student():
    student_id = int(input("Enter student ID: "))
    name = input("Enter new student name: ")
    age = int(input("Enter new student age: "))
    course_name = input("Enter new course name: ")
    instructor_name = input("Enter new instructor name: ")
    Student.update(student_id, name, age, course_name, instructor_name)
    print(f"Student {student_id} updated.")

def update_course():
    course_id = input("Enter course ID: ")
    name = input("Enter new course name: ")
    description = input("Enter new course description: ")
    Course.update(course_id, name, description)
    print(f"Course {course_id} updated.")

def update_instructor():
    instructor_id = input("Enter instructor ID: ")
    name = input("Enter new instructor name: ")
    course_id = input("Enter new course ID: ")
    Instructor.update(instructor_id, name, course_id)
    print(f"Instructor {instructor_id} updated.")

def update_enrollment():
    enrollment_id = input("Enter enrollment ID: ")
    course_name = input("Enter new course name: ")
    instructor_name = input("Enter new instructor name: ")
    Enrollment.update(enrollment_id, course_name, instructor_name)
    print(f"Enrollment {enrollment_id} updated.")

def delete_student():
    student_id = input("Enter student ID to delete: ")
    Student.delete(student_id)
    print(f"Student {student_id} deleted.")

def delete_course():
    course_id = input("Enter course ID to delete: ")
    Course.delete(course_id)
    print(f"Course {course_id} deleted.")

def delete_instructor():
    instructor_id = input("Enter instructor ID to delete: ")
    Instructor.delete(instructor_id)
    print(f"Instructor {instructor_id} deleted.")

def delete_enrollment():
    enrollment_id = input("Enter enrollment ID to delete: ")
    Enrollment.delete(enrollment_id)
    print(f"Enrollment {enrollment_id} deleted.")

def search_students():
    name = input("Enter student name to search: ")
    students = Student.search(name)
    for student in students:
        print(f"Student ID: {student['id']}, Name: {student['name']}, Age: {student['age']}, Course: {student['course_name']}, Instructor: {student['instructor_name']}")

def search_courses():
    name = input("Enter course name to search: ")
    courses = Course.search(name)
    for course in courses:
        print(f"Course ID: {course['id']}, Name: {course['name']}, Description: {course['description']}")

def search_instructors():
    name = input("Enter instructor name to search: ")
    instructors = Instructor.search(name)
    for instructor in instructors:
        print(f"Instructor ID: {instructor['id']}, Name: {instructor['name']}, Course ID: {instructor['course_id']}")

def search_enrollments():
    student_name = input("Enter student name to search (leave blank if not searching by student name): ")
    course_name = input("Enter course name to search (leave blank if not searching by course name): ")
    instructor_name = input("Enter instructor name to search (leave blank if not searching by instructor name): ")
    enrollments = Enrollment.search(student_name, course_name, instructor_name)
    for enrollment in enrollments:
        print(f"Enrollment ID: {enrollment['id']}, Student: {enrollment['student_name']}, Course: {enrollment['course_name']}, Instructor: {enrollment['instructor_name']}")

