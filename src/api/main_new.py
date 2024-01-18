import os

from dotenv import load_dotenv
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

load_dotenv()

app = Flask(__name__)
app.config['SQL_ALCHEMY_TRACK_MODIFICATIONS'] = os.getenv('SQLALCHEMY_TRACK_MODIFICATIONS', default=True)
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.string(80), unique=True, nullable=False)

    def __repr__(self):
        return f'<User {self.username}'


@app.before_request
def create_tables():
    db.create_all()


@app.route('/')
def index():
    users = User.query.all()
    return '\n'.join([user.username for user in users])


if __name__ == '__main__':
    app.run(debug=True)
