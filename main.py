from flask import Flask, request, redirect, render_template

app = Flask(__name__)
app.config['DEBUG'] = True

tasks = []

@app.route('/', methods=['POST', 'GET'])
def index():

    if request.method == 'POST':
        task = request.form['task']
        tasks.append(task)

    return render_template('main_blog.html',title="Build a smegging Blog!", tasks=tasks)


@app.route('/add_blog')
def add_new_post():


    return render_template('add_blog.html')


app.run()