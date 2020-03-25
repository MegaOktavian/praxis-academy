from flask import Flask

app = Flask("coba")

@app.route('/')
def hello():
    return "haaloooooooo"

app.run(debug=True)