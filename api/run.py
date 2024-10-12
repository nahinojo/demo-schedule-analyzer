import os
from waitress import serve

from app import PATH_TO_SCHEDULE, app
from app.database.fill_db_from_calendar import fill_db_from_calendar
from app.routes import api_blueprint
from flask import render_template, send_file

fill_db_from_calendar()
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


if __name__ == '__main__':
    environment = os.environ.get('FLASK_ENV', 'default')
    if environment == 'production':
        serve(app, host='0.0.0.0', port=5000)
    else:
        app.run(host='0.0.0.0')  # 0.0.0.0 necessary to access docker container
