from flask import Flask

app = Flask(__name__)

x = 0


@app.route("/")
def hello_world():
    global x
    x = x + 1
    return f"Call {x}"


app.run(host="0.0.0.0", port=5000)
