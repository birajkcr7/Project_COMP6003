from flask import Blueprint, render_template, request
from models.course import Course

courses_bp = Blueprint('courses', __name__)

@courses_bp.route('/courses')
def search_courses():
    prog_id = request.args.get('prog_id')
    semester = request.args.get('semester')
    courses = []
    
    if prog_id and semester:
        courses = Course.search_courses(prog_id, semester)
    else:
        courses = Course.get_all_courses()
        
    return render_template('courses.html', courses=courses)
