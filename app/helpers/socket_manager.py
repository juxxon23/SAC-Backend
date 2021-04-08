from flask_socketio import SocketIO, join_room, leave_room, send, emit

socketio = SocketIO()


class SocketManager():

    @socketio.on('connect')
    def test_connect(self):
        emit('my response', {'data': 'Connected'})

    @socketio.on('disconnect')
    def test_disconnect(self):
        print('Client disconnected')

    @socketio.on('join')
    def on_join(self, data):
        username = data['username']
        room = data['room']
        join_room(room)
        send(username + ' has entered the room.', room=room)

    @socketio.on('leave')
    def on_leave(self, data):
        username = data['username']
        room = data['room']
        leave_room(room)
        send(username + ' has left the room.', room=room)

    @socketio.on('json')
    def handle_json(self, json):
        print('received json: ' + str(json))

    @socketio.on('sendContent')
    def handle_content(self, data):
        emit('my response', data, broadcast=True)
        
    @socketio.on_error_default  # handles all namespaces without an explicit error handler
    def default_error_handler(self, e):
        print(str(e))


