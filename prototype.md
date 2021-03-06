---
layout: page
title: The Prototype
---

A prototype has been build to validate a couple assumptions taken during the development of the <b>wheelchair++. </b>

The developed prototype will be used to validate the feasibility of the core concept mentioned in the <a href="https://paklongc.github.io/Fitnesswheelchair/2019-09-16-building-foundation/">first post</a>.
To get insights into the desirability of the idea, the ability to measure speed (one of the core functions of the concept) was added to the wheelchair. Since a wheelchair-user uses his/her hands relatively more often; voice recognition and voice output were also added, as an alternate way of interacting. The assumption that this is more desirable, and the aforementioned assumption, will be validated using the prototype.<br>
The results from the (brief) testing and first impressions, regarding the assumptions, are mentioned in the <a href="https://paklongc.github.io/Fitnesswheelchair/2019-11-03-finalizing/">last post</a> in our homepage.

<img src="\Fitnesswheelchair\img\rolstoel.jpg" width="745">


### Sensors and technologies used in final design
<table class="" style="undefined;table-layout: fixed; width: 799px">
<colgroup>
<col style="width: 165px">
<col style="width: 125px">
<col style="width: 390px">
</colgroup>
  <tr>
    <th>Image</th>
    <th>Name</th>
    <th>Role</th>
  </tr>
  <tr>
    <td><img src="\Fitnesswheelchair\img\feather.png" alt=""></td>
    <td>Feather</td>
    <td>The Feather is connected with the Raspberry Pi through bluetooth. the IMU is attached to the Feather. </td>
  </tr>
  <tr>
    <td><img src="\Fitnesswheelchair\img\raspi.png" alt=""></td>
    <td>Raspberry Pi</td>
    <td>The Raspberry Pi is connected to a microphone (webcam), speaker and a server through serial and WiFi. Data collected can be transmitted through Raspberry Pi to the Cloud.</td>
  </tr>
  <tr>
    <td><img src="\Fitnesswheelchair\img\imu.png" alt=""></td>
    <td>IMU Sensor</td>
    <td>The gyro of the IMU is used to measure the angular displacement, so the velocity can be calculated.</td>
  </tr>
  <tr>
    <td><img src="\Fitnesswheelchair\img\snips.png" alt=""></td>
    <td>SNIPS</td>
    <td>SNIPS is used to make voice control possible.</td>
  </tr>
  <tr>
    <td><img src="\Fitnesswheelchair\img\jupy.png" alt=""></td>
    <td>Jupyter Notebook</td>
    <td>Jupyter Notebook is used to visualize a complete .csv-file, making a statistical overview for the user at the end of his/her training.</td>
  </tr>
  <tr>
    <td><img src="\Fitnesswheelchair\img\dcd.png" alt=""></td>
    <td>DCD Hub</td>
    <td>The hub is used to visualize the data live, that is collected and calculated.</td>
  </tr>
</table>
<br>
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
    Data is visualized on the dcdhub and on jupyter notebook.
  </li>
</ul>
