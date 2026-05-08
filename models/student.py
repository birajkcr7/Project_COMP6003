import sqlite3

class Student:
    def __init__(self, studentID, studName, age, email, address, contactNum, marksPercentage, attendancePercentage):
        self.studentID = studentID
        self.studName = studName
        self.age = age
        self.email = email
        self.address = address
        self.contactNum = contactNum
        self.marksPercentage = marksPercentage
        self.attendancePercentage = attendancePercentage

    @staticmethod
    def get_student(student_id):
        with sqlite3.connect('database.db') as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Students WHERE studentID = ?", (student_id,))
            row = cursor.fetchone()
            if row:
                return Student(**dict(row))
        return None

    @staticmethod
    def get_enrollments(student_id):
        enrollments = []
        with sqlite3.connect('database.db') as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            cursor.execute('''
                SELECT c.courseCode, c.courseName 
                FROM Enrollments e
                JOIN Courses c ON e.courseID = c.courseCode
                WHERE e.studentID = ?
            ''', (student_id,))
            enrollments = [dict(row) for row in cursor.fetchall()]
        return enrollments
