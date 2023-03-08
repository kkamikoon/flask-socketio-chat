from flask_socketio import SocketIO

socketio = SocketIO()

@socketio.on('connect')
def connect():
    socketio.emit('my response', {'data': 'Connected'})
