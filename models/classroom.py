import sqlite3

class Classroom:
    def __init__(self, classID, roomNum, buildingNum, seat_capacity, campus):
        self.classID = classID
        self.roomNum = roomNum
        self.buildingNum = buildingNum
        self.seat_capacity = seat_capacity
        self.campus = campus

    @staticmethod
    def get_all_classrooms():
        classrooms = []
        with sqlite3.connect('database.db') as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Classrooms")
            rows = cursor.fetchall()
            for row in rows:
                classrooms.append(Classroom(**dict(row)))
        return classrooms
