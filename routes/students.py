from flask import Blueprint, render_template, request
from models.student import Student

students_bp = Blueprint('students', __name__)

@students_bp.route('/students')
def search_students():
    student_id = request.args.get('student_id')
    student = None
    students = []
    enrollments = []

    if student_id:
        student = Student.get_student(student_id)
        if student:
            enrollments = Student.get_enrollments(student_id)
    else:
        students = Student.get_all_students()

    return render_template(
        'students.html',
        student=student,
        students=students,
        enrollments=enrollments
    )
