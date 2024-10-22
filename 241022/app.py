from flask import Flask

app = Flask(__name__)

x = 0


@app.route("/")
def hello_world():
    x = x + 1
    return "Call $x"
