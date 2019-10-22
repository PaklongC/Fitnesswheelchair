from flask import Flask, render_template, request
from multiprocessing import Process, Value
import time


app = Flask(__name__)

@app.route('/wheelie', methods = ['POST'])
def create():
    print('super hacker')

    return 'Added sensor!'
@app.route('/wheelie', methods = ['GET'])
def getstuff():
    print('super hacker maar net niet')
    return 'learn js'
@app.route('/home')
def home():
    return render_template('index.html')

def record_loop(loop_on):
   while True:
      if loop_on.value == True:
         print("loop running")
      time.sleep(1)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
    
    recording_on = Value('b', True)
    p = Process(target=record_loop, args=(recording_on,))
    p.start()
    app.run(debug=True, use_reloader=False)
    p.join()
