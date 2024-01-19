from flask import Flask
from routes import api
from models import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Disable modification tracking
db.init_app(app)
with app.app_context():
    db.create_all()
app.register_blueprint(api, url_prefix='/api')


@app.route('/test')
def test():
    return "This is my test text"


if __name__ == '__main__':
    app.run(debug=True)
