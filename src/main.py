from flask import Flask, request

app = Flask(__name__)

@app.route('/greet', methods=['GET'])
def greet():
    # Get the 'name' parameter from the query string
    name = request.args.get('name', 'Guest')
    return f'Hello, {name}!'

if __name__ == '__main__':
    app.run(debug=True)

