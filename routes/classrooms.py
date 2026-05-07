from flask import Blueprint, render_template
from models.classroom import Classroom

classrooms_bp = Blueprint('classrooms', __name__)

@classrooms_bp.route('/classrooms')
def list_classrooms():
    classrooms = Classroom.get_all_classrooms()
    return render_template('classrooms.html', classrooms=classrooms)
