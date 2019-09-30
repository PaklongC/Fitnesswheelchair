from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit

app = Flask(__name__)

app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

@app.route('/home')
def home():
    return render_template('index.html')

@app.route('/freekissupercool')
def baas():
    return render_template('gauge.html')

@socketio.on('json')
def handle_json(json):
   print('received json: ' + str(json))
   emit('json', json, broadcast=True)

if __name__ == '__main__':
    # app.run(host='0.0.0.0')
    socketio.run(app, host='0.0.0.0')
