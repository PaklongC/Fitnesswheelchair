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

@app.route('/freekissupercool2')
def graphsfunc():
    return render_template('graphs.html')

@app.route('/freekissupercool3')
def graphsfuncv():
    return render_template('Wheelgraph.html')


@app.route('/d3')
def getD3tut1():
    return render_template('D3tut1.html')

@app.route('/pakswek')
def graphs2():
    return render_template('graph2.html')

@socketio.on('json')
def handle_json(json):
   print('received json: ' + str(json))
   emit('json', json, broadcast=True)

if __name__ == '__main__':
    # app.run(host='0.0.0.0')
    socketio.run(app, host='0.0.0.0')
