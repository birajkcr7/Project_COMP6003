import sqlite3

class Course:
    def __init__(self, courseCode, courseName, num_of_assessments, semester, progID, classID):
        self.courseCode = courseCode
        self.courseName = courseName
        self.num_of_assessments = num_of_assessments
        self.semester = semester
        self.progID = progID
        self.classID = classID

    @staticmethod
    def search_courses(prog_id, semester):
        courses = []
        with sqlite3.connect('database.db') as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            cursor.execute('''
                SELECT * FROM Courses 
                WHERE progID = ? AND semester = ?
            ''', (prog_id, semester))
            rows = cursor.fetchall()
            for row in rows:
                courses.append(Course(**dict(row)))
        return courses
