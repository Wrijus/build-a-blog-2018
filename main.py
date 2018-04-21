from flask import Flask, request, redirect, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://build-a-blog2018:makeit2sec3@localhost:8889/build-a-blog2018'
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)

class Blog(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120))
    body = db.Column(db.String(300))

    def __init__(self, title, body):
        self.title = title
        self.body = body



@app.route('/blog', methods=['POST', 'GET'])
def list_of_posts():
  
    blogs = Blog.query.all()
    if request.args:
        blog_id = request.args.get('id')
        one_entry = Blog.query.filter_by(id=blog_id).first()
        return render_template('entry.html', title="Posted Smeg,", one_entry=one_entry)
    return render_template('blog.html',title="Build a smegging Blog!", blogs=blogs)

      
@app.route('/newpost', methods=['POST', 'GET'])
def add_new_post():


    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']
        new_blog = Blog(title, body)   
        db.session.add(new_blog)
        db.session.commit()

    blogs = Blog.query.all()
    return render_template('newpost.html')

if __name__ == '__main__':
    app.run()