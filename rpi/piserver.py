from flask import Flask, render_template, request
from multiprocessing import Process, Value
from threading import Thread

import time
import wheelie
#import testsub
import threading

thread = None
Wheelie = wheelie
app = Flask(__name__)

@app.route('/wheelie', methods = ['POST'])
def start_dataanalysis():
    print('super hacker')
    #testsub.main()
    recording_on = Value('b', True)
    #p = Process(target=record_loop, args=(recording_on,))
    global thread, Wheelie
    #thread = Thread(target=testsub)
    #thread = Thread(target=subgat.start_connection)
    #thread.start()

    Wheelie.start_data_collection()
    return 'Started sub process data collection'

@app.route('/stop', methods = ['GET'])
def stop():
    global Wheelie
    Wheelie.stop_session()
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
