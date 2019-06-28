from flask import Flask, render_template
from flask_socketio import SocketIO


SECRET_KEY = 'vnkdjnfjknfl1232#'

app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY
socketio = SocketIO(app)


@app.route('/')
def index():
    # return "<h1>cybersecurity s2</h1>"
    return render_template('session.html')


def message_receiver(methods=['GET', 'POST']):
    print('message was received!!!')


@socketio.on('my event')
def handle_my_custom_event(json, methods=['GET', 'POST']):
    print('received my event: ' + str(json))
    socketio.emit('my response', json, callback=message_receiver)


if __name__ == '__main__':
    socketio.run(app, debug=True)
