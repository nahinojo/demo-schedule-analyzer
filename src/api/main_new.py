from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Disable modification tracking
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)

    def __repr__(self):
        return f'<User {self.username}>'


@app.before_request
def create_tables():
    db.create_all()


@app.route('/')
def index():
    # Example: query all users from the 'User' table
    users = User.query.all()
    return '\n'.join([user.username for user in users])


@app.route('/add_user', methods=['POST'])
def add_user():
    data = request.args
    username = data.get('username')

    new_user = User(username=username)
    db.session.add(new_user)
    db.session.commit()

    return f'User {username} added successfully'


if __name__ == '__main__':
    app.run(debug=True)
