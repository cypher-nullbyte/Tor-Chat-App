from flask import Flask


app = Flask(__name__)


@app.route('/')
def index():
    return "<h1>cybersecurity s2</h1>"


app.run()
