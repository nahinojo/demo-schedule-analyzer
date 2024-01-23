from flask import Flask
from routes import test
from models import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Disable modification tracking
db.init_app(app)
with app.app_context():
    db.create_all()

# Registers all routes.
app.register_blueprint(api, url_prefix='/api')


@app.route('/test')
def test():
    return {"status": "success", "message": "Test of Flask Application successfully performed!"}, 200


if __name__ == '__main__':
    app.run(debug=True)
