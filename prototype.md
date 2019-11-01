---
layout: page
title: The Prototype
---

A prototype has been build to validate a couple assumptions taken during the development of the <b>wheelchair++. </b>

The developed prototype will be used to validate the feasibility of the core concept mentioned in the <a href="https://paklongc.github.io/Fitnesswheelchair/2019-09-16-building-foundation/">first post</a>.
To get insights into the desirability of the idea, the ability to measure speed (one of the core functions of the concept) was added to the wheelchair. Since a wheelchair-user uses his/her hands relatively more often; voice recognition and voice output were also added, as an alternate way of interacting. The assumption that this is more desirable, and the aforementioned assumption, will be validated using the prototype.<br>
The results from the (brief) testing and first impressions, regarding the assumptions, are mentioned in the <a href="https://paklongc.github.io/Fitnesswheelchair/2019-11-03-finalizing/">last post</a> in our homepage.

<img src="\Fitnesswheelchair\img\rolstoel.jpg" width="745">


### Research questions related to the prototype
1. Is velocity a relevant measurement when it comes to collecting data from a training?  
  - <i>Getting insight into sensor-activities and measurement accuracy</i>
2. To what extent is voice in and output desirable when it comes to control and output?  
  - <i>Getting insight into analytics</i>


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
