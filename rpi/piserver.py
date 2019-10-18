from flask import Flask, render_template, request
import testsub.py
import threading
app = Flask(__name__)

@app.route('/wheelie', methods = ['POST'])
def create():
    print('super hacker')
    testsub.main()
    return 'Added sensor!'
@app.route('/wheelie', methods = ['GET'])
def getstuff():
    print('super hacker maar net niet')
    return 'learn js'
@app.route('/home')
def home():
    return render_template('index.html')
if __name__ == '__main__':
    app.run(host='0.0.0.0')
