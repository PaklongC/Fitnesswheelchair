---
layout: post
title: Prototype in depth
subtitle: Code explained
bigimg: /img/banner2.png
---
<html>
<div class="row get-started-wrap">
<img src="\Fitnesswheelchair\img\rolstoel.jpg" width="376"> <img src="\Fitnesswheelchair\img\arduinonono.jpg" width="376">
</div>
</html>

### Explanation of our code
The following diagram shows a basic data flow of our prototype
<br>
<img src="\Fitnesswheelchair\img\data_flow.svg" width="750">
<ul>
  <li>
    To activate the data collection a HTTPrequest has to be send to the piserver.py running  a flask server.
    In turn the server will activate wheelie.py
    <br>
    Wheelie.py is the main program responsible for collecting data, saving data, session indexing, sending data to the cloud and sending feedback to the user.
    <br>
    <sup>All local internet devices can start or stop wheelie with http request, we did this to enable support for other platforms and also have a backup when the voice recognition is not working.</sup>
  </li>
  <li>
    Snips communicates through the MQTT broker Hermes, by subscribing or publishing we can get user input or send feedback to the user.
    MQTTsubscribe.js is subscribed to the snips dialog and will forward the intent with HTTPrequests to the local server.
  </li>
  <li>
    Data is collected over Bluetooth from the Adafruit feather that reads the data from the imu sensor
  </li>
  <li>
    Data is saved locally and then send to the cloud
  </li>
  <li>
    Data is visualized on the dcdhub and on jupyter notebook
  </li>
</ul>
