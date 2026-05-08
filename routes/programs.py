from flask import Blueprint, render_template
from models.program import Program

programs_bp = Blueprint('programs', __name__)

@programs_bp.route('/programs')
def list_programs():
    programs = Program.get_all_programs()
    return render_template('programs.html', programs=programs)
