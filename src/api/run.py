from create_app import create_app

app = create_app()

# Registers all routes. Setup for api, not test.
# app.register_blueprint(test, url_prefix='/test')


@app.route('/test')
def test():
    return {"status": "success", "message": "Test of Flask Application successfully performed!"}, 200


if __name__ == '__main__':
    app.run(debug=True)
