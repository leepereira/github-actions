from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_geek():
    return '<h1>Finally working on port 8080 with the team</h2>'


if __name__ == "__main__":
    app.run(port=8080)
