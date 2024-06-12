from database.connection import get_db_connection
from .enrollment import Enrollment

class Student:
    def __init__(self, name, age, course_name, instructor_name):
        self.name = name
        self.age = age
        self.course_name = course_name
        self.instructor_name = instructor_name

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise ValueError("Name must be a string.")
        if len(value) == 0:
            raise ValueError("Name must not be empty.")
        self._name = value

    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, value):
        if not isinstance(value, int):
            raise ValueError("Age must be an integer")
        self._age = value

    @property
    def course_name(self):
        return self._course_name
    
    @course_name.setter
    def course_name(self, value):
        if not isinstance(value, str):
            raise ValueError("Course name must be a string.")
        if len(value) == 0:
            raise ValueError("Course name must not be empty.")
        self._course_name = value

    @property
    def instructor_name(self):
        return self._instructor_name
    
    @instructor_name.setter
    def instructor_name(self, value):
        if not isinstance(value, str):
            raise ValueError("Instructor name must be a string.")
        if len(value) == 0:
            raise ValueError("Instructor name must not be empty.")
        self._instructor_name = value

    def save(self):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO students (name, age, course_name, instructor_name) 
            VALUES (?, ?, ?, ?) 
            ''', (self.name, self.age, self.course_name, self.instructor_name))
        conn.commit()
        conn.close()

    @staticmethod
    def update(student_id, name, age, course_name, instructor_name):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''
            UPDATE students 
            SET name = ?, age = ?, course_name = ?, instructor_name = ? 
            WHERE id = ?
            ''', (name, age, course_name, instructor_name, student_id))
        conn.commit()
        conn.close()

    @staticmethod
    def delete(student_id):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('DELETE FROM students WHERE id = ?', (student_id,))
        conn.commit()
        conn.close()

    @staticmethod
    def all():
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM students')
        students = cursor.fetchall()
        conn.close()
        return students
    
    def __repr__(self):
        return f'<Student {self.name}>'
