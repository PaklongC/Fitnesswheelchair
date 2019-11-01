---
layout: page
title: The Prototype
---

A prototype has been build to validate a couple assumptions taken during the development of the <b>wheelchair++. </b>

The developed prototype will be used to validate the feasibility of the core concept.
To get insights into the desirability of the idea, the ability to measure speed (one of the core functions of the concept) was added to the wheelchair.
Since a wheelchair-user uses his/her hands relatively more often; voice recognition and voice output were also added, as an alternate way of interacting. The assumption that this is more desirable, and the aforementioned assumption, will be validated using the prototype.

![](\Fitnesswheelchair\img\rolstoel.jpg width="745")


### Research questions related to the prototype
1. Is velocity a relevant measurement when it comes to collecting data from a training?  
  - <i>Getting insight into sensor-activities and measurement accuracy</i>
2. To what extent is voice in and output desirable when it comes to control and output?  
  - <i>Getting insight into analytics</i>


### Sensors and technologies used in final design
<table class="" style="undefined;table-layout: fixed; width: 799px">
<colgroup>
<col style="width: 173px">
<col style="width: 138px">
<col style="width: 408px">
</colgroup>
  <tr>
    <th>Image</th>
    <th>Name</th>
    <th>Role</th>
  </tr>
  <tr>
    <td><img src="\Fitnesswheelchair\img\feather.png" alt=""></td>
    <td>Feather</td>
    <td>The Feather is connected with the Raspberry Pi through bluetooth. Sensors are attached to the Feather. Data collected can be transmitted to the Raspberry Pi. </td>
  </tr>
  <tr>
    <td><img src="\Fitnesswheelchair\img\raspi.png" alt=""></td>
    <td>Raspberry Pi</td>
    <td>The Raspberry Pi is connected to a server using Wifi. Data can be transmitted using this.</td>
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
    <td>The hub is used to visualize live the data the is collected and calculated.</td>
  </tr>
</table>
