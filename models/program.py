import sqlite3

class Program:
    def __init__(self, progID, progName, progLevel, duration, totalCredit, num_of_courses):
        self.progID = progID
        self.progName = progName
        self.progLevel = progLevel
        self.duration = duration
        self.totalCredit = totalCredit
        self.num_of_courses = num_of_courses

    @staticmethod
    def get_all_programs():
        programs = []
        with sqlite3.connect('database.db') as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Programs")
            rows = cursor.fetchall()
            for row in rows:
                programs.append(Program(**dict(row)))
        return programs
