from flask import Flask, render_template, request


app = Flask(__name__)

@app.route('/wheelie', methods = ['POST'])
def create():
    print('super hacker pro')
    return 'Added sensor!'

if __name__ == '__main__':
    # app.run(host='0.0.0.0')
    socketio.run(app, host='0.0.0.0')
