from .connection import get_db_connection

def create_tables():
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER NOT NULL,
        course_name TEXT NOT NULL,
        instructor_name TEXT NOT NULL,
        FOREIGN KEY (course_name) REFERENCES courses (name),
        FOREIGN KEY (instructor_name) REFERENCES instructors (name)
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS instructors (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        course_id INTEGER NOT NULL,
        FOREIGN KEY (course_id) REFERENCES courses (id)
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS courses (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        description TEXT NOT NULL
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS enrollments (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        student_name TEXT NOT NULL,
        course_name TEXT NOT NULL,
        instructor_name TEXT NOT NULL,
        FOREIGN KEY (student_name) REFERENCES students (name),
        FOREIGN KEY (course_name) REFERENCES courses (name),
        FOREIGN KEY (instructor_name) REFERENCES instructors (name)
    )
    ''')

    conn.commit()
    conn.close()