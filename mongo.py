from flask import Flask, render_template
from flask_socketio import SocketIO
from pymongo import MongoClient

app = Flask(__name__)
socketio = SocketIO(app)

# MongoDB configuration
client = MongoClient('mongodb://localhost:27017/')
db = client['your_database']

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('message')
def handle_message(msg):
    # Store data in MongoDB
    db.messages.insert_one({'message': msg})
    socketio.emit('message', msg)

if __name__ == '__main__':
    socketio.run(app, debug=True)
