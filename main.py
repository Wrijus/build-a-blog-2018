from flask import Flask, request, redirect, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://build-a-blog2018:makeit2sec3@localhost:8889/build-a-blog2018'
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)

class Task(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120))

    def __init__(self, name):
        self.name = name



@app.route('/blog', methods=['POST', 'GET'])
def list_of_posts():

    if request.method == 'POST':
        task_name = request.form['task']
        new_task = Task(task_name)
    
    tasks = Task.query.all()

    return render_template('blog.html',title="Build a smegging Blog!", tasks=tasks)


@app.route('/newpost', methods=['POST', 'GET'])
def add_new_post():


    if request.method == 'POST':
        task_name = request.form['task']
        new_task = Task(task_name)        
        db.session.add(new_task)
        db.session.commit()

    tasks = Task.query.all()

    return render_template('newpost.html')

if __name__ == '__main__':
    app.run()