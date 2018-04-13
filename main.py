from flask import Flask, request, redirect, render_template

app = Flask(__name__)
app.config['DEBUG'] = True

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


app.run()