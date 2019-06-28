from flask import Flask
import datetime
import urllib.parse


SEP = '-$$-$$-'
LINE_B = '-@@-@@-'

line = '2019-06-27 23:48:47.678' + SEP + 'carl' + SEP + 'this is a message'
talk = [line, line, line]
app = Flask(__name__)


@app.route('/')
def index():
    return LINE_B.join(talk)


@app.route('/user/<user>/message/<message>')
def show_post(user, message):
    user = urllib.parse.unquote(user)
    message = urllib.parse.unquote(message)
    time = str(datetime.datetime.now())
    talk.append(SEP.join([time, user, message]))
    return LINE_B.join(talk)


app.run()
