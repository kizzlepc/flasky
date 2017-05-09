from flask import Flask,make_response,redirect,abort
from flask.ext.script import Manager

app = Flask(__name__)
manager = Manager(app)

@app.route('/')
def index():
    return '<h1>Hello,World!</h1>'


@app.route('/user/<name>')
def user(name):
    return '<h1>Hello,%s!</h1>'%name


@app.route('/user/<ids>')
def get_user(ids):
    user = load_user(ids)
    if not user:
        abort(404)
    return '<h1>Hello,%s!</h1>'%user.name

if __name__ == '__main__':
    #app.run(debug = True)
    manager.run()
