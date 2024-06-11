from database.connection import get_db_connection

class Enrollment:
    def __init__(self, student_name, course_name, instructor_name):
        self.student_name = student_name
        self.course_name = course_name
        self.instructor_name = instructor_name

    def save(self):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''
        INSERT INTO enrollments(student_name, course_name, instructor_name)
        VALUES (?, ?, ?)
        ''', (self.student_name, self.course_name, self.instructor_name))
        conn.commit()
        conn.close()

    @staticmethod
    def all():
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''
        SELECT e.id, e.student_name, e.course_name, e.instructor_name, s.age, c.description
        FROM enrollments e
        JOIN students s ON e.student_name = s.name
        JOIN courses c ON e.course_name = c.name
        JOIN instructors i ON e.instructor_name = i.name
        ''')
        enrollments = cursor.fetchall()
        conn.close()
        return enrollments
