---
layout: post
title: Data visualization
subtitle: D3.js, DCD Hub and Jupyter Notebook
---

Data transferred can be visualized using several methods.

#### 1. D3.js
D3.js offers an extensive library with widgets, build up from several different .html-, .css-, .js- and other files.<br>
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
<sup>Snippet of our Python code, full code can be found in web\server4.py of our <a href="https://github.com/PaklongC/Fitnesswheelchair/blob/master/web/server4.py">GitHub</a> (see the link in our header)</sup>

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
<sup>Snippet of our Javascript code, full code can be found in web\templates\Wheelgraph.html of our <a href="https://github.com/PaklongC/Fitnesswheelchair/blob/master/web/templates/Wheelgraph.html">GitHub</a> (see the link in our header)</sup><br>
Other files and examples can be found in the web folder of our Github.<br>
Using the <i>"Simple Graph"</i> widget, combined with data transferred in a .csv-file, the following graph could be created:

<img src="\Fitnesswheelchair\img\d3graph.png" alt="">
<b>Although many projects have successfully implemented D3.js widgets into their projects. Due to the scope of the project, we felt that the returns of using such a complex system was not efficient enough with regards to the time we had.</b>

#### 2. Jupyter Notebook
Jupyter Notebook offers a plugin where widgets can be quickly implemented and viewed in the same 'page' it has been coded. This can be done relatively easily and quickly with the right (versions of) packages installed. Different widgets can complement each other, creating an dashboard where all datasets can be shown.<br>

```python
import ipywidgets as widgets
from ipywidgets import interactive, interact, interact_manual
import plotly.express as px

df_root = pd.read_csv('Rootfolder.csv')

def selected_workout(array):
    unique = array.unique().tolist()
    unique.sort()
    unique.insert(0, "Workout")
    return unique

dropdown_file = widgets.Dropdown(options = selected_workout(df_root.filename))

output_file = widgets.Output()

def dropdown_file_eventhandler(change):
    output_file.clear_output()
    with output_file:
        if (change.new=="Workout"):
            print('select your workout')
        else:
            global df_plot
            df_plot=pd.read_csv(change.new)
            fig1 = px.line(df_plot, x = 'time', y = 'velocity', title='Workout ')
            fig1.show()

dropdown_file.observe(dropdown_file_eventhandler, names='value')

display(dropdown_file)
```
<sup>Snippet of our Python code, full code can be found in \FINAL 1.1.ipynb of our <a href="https://github.com/PaklongC/Fitnesswheelchair/blob/master/Untitled.ipynb">GitHub</a> (see the link in our header)</sup><br>

This part of the code will create a dropdown with all the 'workout' files that are stored. By selecting one, the data from the .csv file is visualized in a plot. The visualization is shown in the following dashboard: 

<img src="\Fitnesswheelchair\img\Jupyter_Dashboard.png" width="745">
<b>This feature offers great features for the scope of this project/prototype. Although making the visualization live is more challenging, data can be visualized cleanly of one .csv-file.
Several other widgets (like a dropdown) are also available. Although visualizations are not live, several different .csv-files can be rendered when the right option is chosen from a drop-down.</b>

#### 3. DCD Hub
When connected, the DCD Hub offers easy live interactable visualizations of data received.

<img src="\Fitnesswheelchair\img\dcdgraph.png" width="745">

<b>Getting everything going might prove troublesome at the beginning. However, the returns are great since live visualizations are still (relatively) easily established.</b>
