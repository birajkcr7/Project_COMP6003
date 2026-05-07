from flask import Flask, render_template
import sqlite3

def create_app():
    app = Flask(__name__)
    
    # Register blueprints

    
    
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
                
                
        except sqlite3.Error:
            stats = {}
            
        return render_template('index.html', stats=stats)
        
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
