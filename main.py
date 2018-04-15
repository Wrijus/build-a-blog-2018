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

tasks = []

@app.route('/', methods=['POST', 'GET'])
def list_of_posts():



    return render_template('main_blog.html',title="Build a smegging Blog!", tasks=tasks)


@app.route('/add_blog', methods=['POST', 'GET'])
def add_new_post():


    if request.method == 'POST':
        task = request.form['task']
        tasks.append(task)

    return render_template('add_blog.html', tasks=tasks)

if __name__ == '__main__':
    app.run()