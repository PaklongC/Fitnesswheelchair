from flask import Flask, render_template, request
from multiprocessing import Process, Value
from threading import Thread
import time
#import subgat
import testsub
import threading

thread = None

app = Flask(__name__)

def record_loop(loop_on):
   while True:
      if loop_on.value == True:
         print("loop running")
      time.sleep(1)

@app.route('/wheelie', methods = ['POST'])
def start_dataanalysis():
    print('super hacker')
    #testsub.main()
    recording_on = Value('b', True)
    #p = Process(target=record_loop, args=(recording_on,))
    global thread
    thread = Thread(target=testsub)
    thread.start()
    print("t1")
    # app.run(debug=True, use_reloader=False)
    print("t2")
    print("t3")
    return 'Started sub process data collection'

@app.route('/stop', methods = ['GET'])
def stop():
    thread.cancel()
    return 'stopped'

@app.route('/wheelie', methods = ['GET'])
def getstuff():
    print('super hacker maar net niet')
    return 'learn js'

@app.route('/home')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0',use_reloader=False)
