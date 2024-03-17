from flask import send_file

from app import app, PATH_TO_SCHEDULE
from app.database.setup_db import setup_db
from app.routes import api_blueprint

setup_db()
app.register_blueprint(api_blueprint, url_prefix='/api')


@app.route('/download_schedule')
def download_schedule():
    return send_file(PATH_TO_SCHEDULE, as_attachment=True)


app.run()
