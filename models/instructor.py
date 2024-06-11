from database.connection import get_db_connection

class Instructor:
    def __init__(self, name, course_id):
        self.name = name
        self.course_id = course_id

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
    def course_id(self):
        return self._course_id
    
    @course_id.setter
    def course_id(self, value):
        if not isinstance(value, int):
            raise ValueError("Id must be an integer")
        self._course_id = value

    def save(self):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''
        INSERT INTO instructors(name, course_id)
        VALUES (?, ?)
        ''', (self.name, self.course_id))
        conn.commit()
        conn.close()

    @staticmethod
    def all():
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM instructors')
        instructors = cursor.fetchall()
        conn.close()
        return instructors
    
    def __repr__(self):
        return f'<Instructor {self.name}>'
