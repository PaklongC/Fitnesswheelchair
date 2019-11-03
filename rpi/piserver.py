from flask import Flask, render_template, request
from multiprocessing import Process, Value
from threading import Thread

import time,os,json,csv
import wheelie
#import testsub
import threading

thread = None
Wheelie = wheelie
app = Flask(__name__)

@app.route('/wheelie', methods = ['GET'])
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
    thread = Thread(target=wheelie.stop_session)
    thread.start()
    #Wheelie.stop_session()
    return 'stopped'

@app.route('/getIndex', methods = ['GET'])
def get_session_index():
    indexPath = os.path.join(os.path.dirname(os.path.abspath(__file__)),"rpi","session_index.csv")
    try:
        with open(indexPath, 'r') as f:
            reader = csv.reader(f)
            session_index = list(reader)
            f.close()
        print("HTTP send from",indexPath,":",session_index)
    except: print("could not get session index from:",indexPath)
    return json.dumps(session_index)

@app.route('/getSessionData', methods = ['GET'])
def get_session_data():
    #print("HTTP send from",sessionPath,":",session_index)
    sessionFileName = request.args.get('csvName', default="defaultdata.csv", type=str)
    sessionPath = os.path.join(os.path.dirname(os.path.abspath(__file__)),"rpi","data",sessionFileName)

    with open(sessionPath, 'r') as sf:
        reader = csv.reader(sf)
        session_Data = list(reader)
        sf.close()
    return json.dumps(session_Data)

@app.route('/home')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0',use_reloader=False)
