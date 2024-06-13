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
    def update(enrollment_id, course_name, instructor_name):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''
            UPDATE enrollments 
            SET course_name = ?, instructor_name = ? 
            WHERE id = ?
            ''', (course_name, instructor_name, enrollment_id))
        conn.commit()
        conn.close()

    @staticmethod
    def delete(enrollment_id):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('DELETE FROM enrollments WHERE id = ?', (enrollment_id,))
        conn.commit()
        conn.close()


    @staticmethod
    def all():
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''
        SELECT e.id, e.student_name, e.course_name, e.instructor_name, s.age, c.description
        FROM enrollments e
        INNER JOIN students s ON e.student_name = s.name
        INNER JOIN courses c ON e.course_name = c.name
        INNER JOIN instructors i ON e.instructor_name = i.name
        ''')
        enrollments = cursor.fetchall()
        conn.close()
        return enrollments
    
    @staticmethod
    def search(student_name=None, course_name=None, instructor_name=None):
        conn = get_db_connection()
        cursor = conn.cursor()
        query = 'SELECT * FROM enrollments WHERE 1=1'
        params = []
        if student_name:
            query += ' AND student_name LIKE ?'
            params.append('%' + student_name + '%')
        if course_name:
            query += ' AND course_name LIKE ?'
            params.append('%' + course_name + '%')
        if instructor_name:
            query += ' AND instructor_name LIKE ?'
            params.append('%' + instructor_name + '%')
        cursor.execute(query, params)
        enrollments = cursor.fetchall()
        conn.close()
        return enrollments
