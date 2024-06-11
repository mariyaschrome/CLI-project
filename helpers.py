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