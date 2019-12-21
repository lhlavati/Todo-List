from flask import Flask, render_template, render_template
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////home/student/Todo List/todo.db'

db = SQLAlchemy(app)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(200))
    computer = db.Column(db.Boolean)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add', methods=['POST'])
def add():
    return '<h1>{}</h1>'.format(request.form['todoitem'])

if __name__ == '__main__':
    app.run(debug=True)