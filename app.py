from flask import Flask, render_template
import sqlite3

def create_app():
    app = Flask(__name__)
    
    # Register blueprints
    from routes.programs import programs_bp
    from routes.courses import courses_bp
    from routes.students import students_bp
    from routes.classrooms import classrooms_bp
    
    app.register_blueprint(programs_bp)
    app.register_blueprint(courses_bp)
    app.register_blueprint(students_bp)
    app.register_blueprint(classrooms_bp)
    
    
    @app.route('/')
    def home():
        return render_template('home.html')

    @app.route('/dashboard')
    def dashboard():
        stats = {}
        try:
            with sqlite3.connect('database.db') as conn:
                conn.row_factory = sqlite3.Row
                cur = conn.cursor()
                
                cur.execute("SELECT COUNT(*) as count FROM Programs")
                stats['programs'] = cur.fetchone()['count']
                
                cur.execute("SELECT COUNT(*) as count FROM Courses")
                stats['courses'] = cur.fetchone()['count']
                
                cur.execute("SELECT COUNT(*) as count FROM Students")
                stats['students'] = cur.fetchone()['count']
                
                cur.execute("SELECT COUNT(*) as count FROM Classrooms")
                stats['classrooms'] = cur.fetchone()['count']
                
        except sqlite3.Error:
             stats = {'programs': 0, 'courses': 0, 'students': 0, 'classrooms': 0}
            
        return render_template('index.html', stats=stats)
        
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
