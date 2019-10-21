import datetime

import dash
from dash.dependencies import Output, Input
import dash_core_components as dcc
import dash_html_components as html
import plotly
import plotly.graph_objs as go
from collections import deque

import pygatt
import signal
import os
import time

#================BLUETOOTH MODULE====================

BLUETOOTH_DEVICE_MAC ="F4:36:23:1E:9E:54"

ATT_CHARACTERISTIC_ORIENTATION ="02118833-4455-6677-8899-AABBCCDDEEFF"
DDRESS_TYPE = pygatt.BLEAddressType.random

def handle_orientation_data(handle, value_bytes):
    print("Received data: %s (handle %d)" % (str(value_bytes), handle))
    values = [float(x) for x in value_bytes.decode('utf-8').split(",")]
    speed = values[1]

def discover_characteristic(device):
    for uuid in device.discover_characteristics().keys():
        try:
            print("Read UUID" + str(uuid) + "   " + str(device.char_read(uuid)))
        except:
            print("Something wrong with " + str(uuid))

def read_characteristic(device, characteristic_id):
    return device.char_read(characteristic_id)

def keyboard_interrupt_handler(signal_num, frame):
    print("Exiting...".format(signal_num))
    left_wheel.unsubscribe(GATT_CHARACTERISTIC_ORIENTATION)
    exit(0)

bleAdapter = pygatt.GATTToolBackend()
bleAdapter.start()

a = 1
b = 1
c = 1
d = 0

#Connect bluetooth device
while a:
    try:
        left_wheel = bleAdapter.connect(BLUETOOTH_DEVICE_MAC, address_type=ADDRESS_TYPE)
        print("Connection succesfull:" +str(BLUETOOTH_DEVICE_MAC) )
        a = 0
    except:
        print("whooopie daisy no connection")
        time.sleep(5)

# Subscribe to the GATT service
while b: #try this for 30 times
    try:
        print("try data subscribe")
        left_wheel.subscribe(GATT_CHARACTERISTIC_ORIENTATION,
                         callback=handle_orientation_data)
        b = 0
    except:
        print("Trying to figure stuff out" + str(d))
        d = d + 1
        if(d>=30):
            b = 0
        time.sleep(1)

while True:
    print(speed)
    time.sleep(1)



# Register our Keyboard handler to exit
signal.signal(signal.SIGINT, keyboard_interrupt_handler)

#===============LIVE GRAPH================

X = deque(maxlen=20)
X.append(1)
Y = deque(maxlen=20)
Y.append(1)

app = dash.Dash(__name__)
app.layout = html.Div(
    [
        dcc.Graph(id='live-graph', animate=True),
        dcc.Interval(
            id='graph-update',
            interval=1*200
        ),
    ]
)

@app.callback(Output('live-graph', 'figure'),
              [Input('graph-update', 'interval')])
def update_graph_scatter():
    time = datetime.datetime.now().strftime('%D, %H:%M:%S')
    X.append(time)
    Y.append(speed)

    data = plotly.graph_objs.Scatter(
            x=list(X),
            y=list(Y),
            name='Scatter',
            mode= 'lines+markers'
            )

    return {'data': [data],'layout' : go.Layout(xaxis=dict(range=[min(X),max(X)]),
                                                yaxis=dict(range=[min(Y),max(Y)]),)}



if __name__ == '__main__':
    app.run_server(debug=True)
