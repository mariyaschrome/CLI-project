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