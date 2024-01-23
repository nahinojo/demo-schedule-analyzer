from database import db
from create_app import create_app

import pytest

app = create_app()


@app.route('/test')
def test():
    return {"status": "success", "message": "Test of Flask Application successfully performed!"}, 200


if __name__ == '__main__':
    app.run(debug=True)
