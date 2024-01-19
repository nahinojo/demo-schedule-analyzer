from flask import Flask
from routes import add_test_course, get_courses
from models import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Disable modification tracking
db.init_app(app)


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
    all_courses = get_courses()
    print("all_courses:", all_courses)
    return all_courses


@app.route('/add_a_test_course', methods=['POST'])
def add_a_test_course():
    add_test_course()
    return f'test course added successfully'


if __name__ == '__main__':
    app.run(debug=True)
