from flask import Flask, render_template, render_template_string, request

from .db import db
from .models import Post

app = Flask(__name__)
app.config.from_pyfile('config.py')
db.init_app(app)

@app.route('/input')
def input():
    return '''
    <form method="post" action="/test">
        <input type="text" name="name" placeholder="Enter your name">
        <input type="submit" value="Submit">
    </form>
    '''

@app.route('/test', methods=['POST'])
def test():
    name = request.form['name']
    template = f"Hello, {name}!"
    return render_template_string(template)
    # return render_template('hello.html', name=name)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        text = request.form['text']
        post = Post(text)
        db.session.add(post)
        db.session.commit()
    posts = Post.query.order_by(Post.date_posted.desc()).all()
    return render_template('index.html', posts=posts)


if __name__ == '__main__':
    app.run()
