from flask import Flask, request, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/home')
def home():
    return render_template('index.html')

@app.route('/freekissupercool')
def baas():
    return render_template('gauge.html')

@app.route('/freekissupercool2')
def baas2():
    return render_template('graphs.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0')
