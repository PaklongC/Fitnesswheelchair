---
layout: post
title: Data visualization
subtitle: D3.js, DCD Hub and Jupyter Notebook
---

Data transferred through <b>FIXMEEEEE</b> can be visualized using several methods.

#### 1. D3.js
D3.js offers an extensive library with widgets, build up from several different .html-, .css-, .js-files etcetera.
Snippet of python code, full code can be found in web\server4.py of our GitHub (see the link in our header):
```python
from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit

app = Flask(__name__)

app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

@app.route('/home')
def home():
    return render_template('index.html')
```
Snippet of javascript code, full code can be found in web\templates\Wheelgraph.html of our GitHub (see the link in our header):
```javascript
      d3.csv("{{ url_for('static', filename='text/pidata3.csv') }}", function(error, data) {
        if (error) throw error;
        data.forEach(function(d) {
          d.t = d.t;
          d.v = d.v;
        });
        svg.append("path")
          .data([data])
          .attr("class", "line")
          .attr("d", valueline);
      };  
```
Other files and examples can be found in the web folder of our Github.

Using the <i>"Simple Graph"</i> widget, combined with data transferred in a .csv-file, the following graph could be created
<img src="\Fitnesswheelchair\img\hpvisual.png" alt="600">fixme graph

<b>Although many projects have successfully implemented D3.js widgets into their projects. Due to the scope of the project, we felt that the returns of using such a complex system was not efficient enough with regards to the time we had.</b>

#### 2. Jupyter Notebook
Jupyter Notebook offers a plugin where widgets can be viewed in the same 'page' it has been coded. This can be done relatively easily and quickly when the right (versions of) packages are installed.
Snippet of python code, full code can be found in \Untitled.ipynb of our GitHub (see the link in our header):
```python
plt.plot(t,data_frame.y)
data_frame = pd.DataFrame(data[:,1:], index = pd.DatetimeIndex(pd.to_datetime(data[:,0], unit='ms')))
pd.DataFrame.describe(data_frame)
```
Also, by adding analytics-libraries, different statistics can be calculated and shown.
<img src="\Fitnesswheelchair\img\hpvisual.png" alt="600">fixme graph

<b>This feature offers great features for the scope of this project/prototype. Although making the visualization live is more challenging, data can be visualized cleanly of one .csv-file.
Several other widgets (like a dropdown) are also available. Although visualizations are not live, several different .csv-files can be rendered when the right option is chosen from a drop-down.</b>

#### 3. DCD Hub
When connected, the DCD Hub offers easy live visualizations of data received.
<img src="\Fitnesswheelchair\img\hpvisual.png" alt="600">fixme graph

<b>Getting everything going might prove troublesome at the beginning. However, the returns are great since live visualizations are still (relatively) easily established.</b>
