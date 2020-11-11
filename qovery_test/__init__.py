import os

from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['QOVERY_DATABASE_MY_DB_CONNECTION_URI']
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username


db.create_all()

if User.query.count() == 0:
    for username in ('admin', 'guest'):
        user = User(username=username, email=f'{username}@example.com')
        db.session.add(user)
        db.session.commit()


@app.route('/')
def root():
    return jsonify('root endpoint')


@app.route('/users')
def users():
    users = db.session.query(User).all()
    return jsonify({
        'users': [{
            'username': user.username,
            'email': user.email
        } for user in users]
    })


@app.route('/shell')
def shell():
    raise ValueError
