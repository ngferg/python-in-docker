from flask import Flask
import src.greeter

app = Flask(__name__)

greeter = src.greeter.Greeter()

@app.route('/greet')
def hello_world():
    return greeter.hello_world()

@app.route('/greet/<name>')
def greet(name: str):
    return greeter.greet(name)

@app.route('/greet/<name>/reset', methods=['PATCH'])
def reset(name: str):
    res = greeter.reset(name)
    return res

@app.after_request
def add_header(response):
    response.headers['Content-Type'] = 'application/json'
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050)
