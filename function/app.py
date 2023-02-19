from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_geek():
    return '<h1>From my work laptop </h2>'


if __name__ == "__main__":
    app.run(port=8080)
