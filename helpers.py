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
