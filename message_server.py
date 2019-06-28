from flask import Flask
import datetime


talk = []
sep = '-$$-$$-'
app = Flask(__name__)


@app.route('/')
def index():
    return '\n'.join(talk)


@app.route('/user/<user>/message/<message>')
def show_post(user, message):
    time = str(datetime.datetime.now())
    talk.append(sep.join([time, user, message]))
    return '\n'.join(talk)


app.run()
