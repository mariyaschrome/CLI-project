from database.connection import get_db_connection

class Course:
    def __init__(self, name, description):
        self.name = name
        self.description = description

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
    def description(self):
        return self._description
    
    @description.setter
    def description(self, value):
        if not isinstance(value, str):
            raise ValueError("Description must be a string")
        if len(value) == 0:
            raise ValueError("Description must not be empty")
        self._description = value

    def save(self):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''
        INSERT INTO courses(name, description)
        VALUES (?, ?)
        ''', (self.name, self.description))
        conn.commit()
        conn.close()

    @staticmethod
    def update(course_id, name, description):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''
            UPDATE courses 
            SET name = ?, description = ? 
            WHERE id = ?
            ''', (name, description, course_id))
        conn.commit()
        conn.close()

    @staticmethod
    def delete(course_id):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('DELETE FROM courses WHERE id = ?', (course_id,))
        conn.commit()
        conn.close()

    @staticmethod
    def all():
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM courses')
        courses = cursor.fetchall()
        conn.close()
        return [dict(course) for course in courses]
    
    def __repr__(self):
        return f'<Course {self.name}>'