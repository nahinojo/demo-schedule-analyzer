from flask import send_file, render_template

from app import app, PATH_TO_SCHEDULE
from app.database.setup import setup
from app.routes import api_blueprint

setup()
app.register_blueprint(api_blueprint, url_prefix='/api')


@app.route('/download_schedule')
def download_schedule():
    return send_file(PATH_TO_SCHEDULE, as_attachment=True)


@app.route('/test')
def test():
    return "Test API route successful!"


@app.route('/')
def homepage():
    return render_template('index.html')


app.run()
