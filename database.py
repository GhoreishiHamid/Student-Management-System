import sqlite3


DATABASE_NAME = "data/students.db"


def connect_db():
    return sqlite3.connect(DATABASE_NAME)


def create_tables():
    connection = connect_db()
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            student_id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            major TEXT NOT NULL
        )
    """)

    connection.commit()
    connection.close()


def add_student(student):
    connection = connect_db()
    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO students (student_id, name, email, major)
        VALUES (?, ?, ?, ?)
    """, (
        student.student_id,
        student.name,
        student.email,
        student.major
    ))

    connection.commit()
    connection.close()

def get_students():
    connection = connect_db()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT student_id, name, email, major
        FROM students
    """)

    students = cursor.fetchall()

    connection.close()

    return students


def search_student(student_id):
    connection = connect_db()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT student_id, name, email, major
        FROM students
        WHERE student_id = ?
    """, (student_id,))

    student = cursor.fetchone()

    connection.close()

    return student