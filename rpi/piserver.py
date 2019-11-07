from flask import Flask, render_template, request
from multiprocessing import Process, Value
from threading import Thread

import time,os,json,csv
import wheelie
import threading

thread = None
Wheelie = wheelie
app = Flask(__name__)

#HTTP request listener that starts wheelie
#currently wheelie is setup to start connecting and then start data collection
#we highly recommend to seperate the connection and data collection to prevent to constantly have to reconnect to bluetooth
#so define 2 more intents wheelieConnect, wheelieDisconnect
@app.route('/wheelie', methods = ['GET'])
def start_dataanalysis():
    print('Starting workout session')
    recording_on = Value('b', True)
    global Wheelie
    Wheelie.start_data_collection()
    return 'Started sub process data collection'

#HTTP request listener that stops wheelie
@app.route('/stop', methods = ['GET'])
def stop():
    global Wheelie

    #run a thread that stops our current wheelie data collection
    thread = Thread(target=wheelie.stop_session)
    thread.start()
    return 'stopped'
    
#HTTP request listener that returns the saved index of all the workout sessions from session_index.csv
@app.route('/getIndex', methods = ['GET'])
def get_session_index():
    #set our index path
    indexPath = os.path.join(os.path.dirname(os.path.abspath(__file__)),"rpi","session_index.csv")
    try:
        #read our index and put it in an list: session_index
        with open(indexPath, 'r') as f:
            reader = csv.reader(f)
            session_index = list(reader)
            f.close()
        print("HTTP send from",indexPath,":",session_index)
    except: print("could not get session index from:",indexPath)
    #Send the session_index list as an json to the client
    return json.dumps(session_index)

#HTTP request listener that returns the saved workout data
@app.route('/getSessionData', methods = ['GET'])
def get_session_data():
    #convert the optional args from the url to get the specific session name
    #if none use defaultdata.csv
    sessionFileName = request.args.get('csvName', default="defaultdata.csv", type=str)

    #set the path where we get the session data from
    sessionPath = os.path.join(os.path.dirname(os.path.abspath(__file__)),"rpi","data",sessionFileName)
    #open the file and convert it to a list
    with open(sessionPath, 'r') as sf:
        reader = csv.reader(sf)
        session_Data = list(reader)
        sf.close()
    #return the session data as an json to the client
    return json.dumps(session_Data)

@app.route('/home')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0',use_reloader=False)
