from flask import Flask, request, render_template, redirect, url_for, session
from flask_socketio import SocketIO, join_room, leave_room, send


from utils import generate_room_code


app = Flask(__name__)
app.config['SECRET_KEY'] = 'jkfjkl;asdjkajklafsklfdjklf'
socketio = SocketIO(app)

rooms = {}  

# TODO : Build Routes

# TODO : Build SocketIO Events


if __name__ == '__main__':
    socketio.run(app, debug=True)

