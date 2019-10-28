---
layout: page
title: Read me md-file
subtitle: README
bigimg: /img/start.jpg
---
<!DOCTYPE html>
<html>
<head>
<title>Fitnesswheelchair</title>
</head>
<h1>Fitnesswheelchair</h1>
<h6>By Pak Long, Freek and Lorenzo</h6>
<img src="Images/banner.png" width="" height="">
<hr>
<body>

<h3>Scope:</h3>
<H8><b>WHAT</b></H8>
<img src="Images/fitnessChair.png" width="" height="">

<head>
<style type="text/css">
.list {
 float:left;
 width:49.9%;
}
</style></head>

<div id="container">
  <div class="list">
	<ul>
	  <ul><H8><b>WHY</b></H8></ul><br>
	  <li>Create a wheelchair that functions as a fitness tracker for the disabled by measuring their development and performances. The prototype serves to test the feasibility of one of the core features of the concept.</li>
	</ul>
  </div>
  <div class="list">
	<ul>
	  <ul><H8><b>HOW</b></H8></ul><br>
	  <li> Testing the accelerometer and force sensor to collect meaningful data to send to the HUB.
      </li>
      <ul>
        <li>Getting insight into sensor-sensitivities and accurate measurements.<br>
      </ul></li></li>
	  <li>Using the data during exercise with voice control.</li>
    <ul>
      <li>Getting insight into the user-interaction, guided by sound.</li>
    </ul><br></li>
	</ol>
  </div>
  <br style="clear:both" />
</div>
</body>

<img src="Images\IOT Architecture.png" width="" height="">
<img src="Images\speedTime.png" width="" height="">
<hr>
<h3>Sensor analysis:</h3>

<table style="width:100%">
  <tr>
    <th>Sensor/Actuator Used</th>
    <th>Data collected/needed</th>
    <th>Method</th>
    <th>Pros & Cons</th>
    <th>Take-aways</th>
  </tr>
  <tr>
    <td rowspan = 3>IMU<br><img src="Images/IMU.png" width="" height=""></td>
    <td>- Acceleration > Velocity</td>
    <td>Integral approach by calculating the sum of velocities-values between certain time-points using the acceleration.</td>
    <td><b>+ </b>Velocity is constantly being calculated<br><b>- </b>This method is very dependant on the sensitivity of the accelerometer and its (correct) calibration. Because the sum of the measured and calculated values are used, little measurement-errors will lead to bigger and bigger deviations</td>
    <td><img src="" width="" height=""></td>
  </tr>
  <tr>
    <td rowspan = 1>- Rotation time > Velocity</td>
    <td>'RPM-'approach by calculating the velocity using wheelchair-specific properties.</td>
    <td><b>+ </b>This method is relatively more accurate because the turn-rate can be measured more reliably<br><b>- </b>Because (1/f=T) is used, the speed can only be calculated when one whole rotation of the wheel is made</td>
    <td><img src=""></td>
  </tr>
  <tr>
    <td>- Radial displacement > Velocity</td>
    <td>Differential approach by making use of the tangents.</td>
    <td><b>+ </b>Velocity is constantly being calculated<br><b>- </b>This method is very dependant on the sensitivity of the accelerometer and its (correct) calibration (<-- angle measurements have relatively less fluctuations in values than acceleration)</td>
    <td><img src=""></td>
  </tr>
  <tr>
    <td rowspan = 2>Speaker<br><img src="Images/speaker.png" width="200" height=""><br><br>Microphone<br><img src="Images/soundSensor.png" width="200" height=""></td>
    <td></td>
    <td>USB-speaker to give feedback to the user </td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td></td>
    <td> Webcam microphone to get voice input from the user</td>
    <td></td>
    <td></td>
  </tr>
   <tr>
    <td><img src="https://miro.medium.com/max/400/1*lfbfrWS3PUaO3BX3ob1ZYQ.png" width="200" height=""></td>
    <td>- Voice ></td>
    <td>Easy to use web platform with great custom voice recognition</td>
    <td>
      <ul>
        <li>Sam to setup local services </li>
        <li>Hermes to communicate over MQTT with snips</li>
        <li>local flask server with http requests to communicate with python script and hermes javascript<li>
      </ul>
     </td>
  </tr>
  <tr>
    <td rowspan = 2>D3.js<br><img src="Images/d3js.png" width="200" height=""><br><br>Data-centric Design Hub<br><img src="Images/dcd.png" width="200" height=""></td>
    <td>- Accumulated data stored in a CSV-file</td>
    <td>Drawing a graph of the 'total workout' using the aforementioned CSV</td>
    <td>- As the code is now, the graph serves as a total overview rather than something that is regularly updated live</td>
    <td><img src=""></td>
  </tr>
  <tr>
    <td></td>
    <td>- Voice > recogition</td>
    <td>Using the API provided by google</td>
    <td></td>
  </tr>
</table>
<hr>
<h2> To do:</h2>
<ul>
  <li><strike>DCD Hub, (hoogste prio want dan hoeven we zelf geen grafieken te maken maar dan moet deze het wel doen)</li>
  <li>Grafieken, (kan met d3.js maar zoek ff een tutorial want is best lastig)</strike></li>
  <li>Data analyse, ok we hebben data wat doen we er mee? Bedenk wat we willen doen (visueel diagram) Als we dat weten kunnen bij subgat.py functies schrijven maak wel ff een backup van subgat.py </li>
  <li>Communicatie javascript naar python. (Nu een flask server op rpi/piserver.py deze accepteerd httprequest zoals http://<IPADRESS:500>/wheelie "post" en print dan "supper hacker pro". (dit lukte binnen 1x dus was idd best wel super hacker pro).
    Nu moet javascript nog een httpresquest posten naar de python server. (javascript runnen door in terminal: node scriptnaam.js) server runnen met python3: rpi/piserver.py (dit kan je allemaal op je laptop doen maar dan moet je wel node.js en flask instaleren, kan ook op pi daar staat het al</li>
  <li>Http request sturen van voice control (snips) naar piserver.py vanuit index.js (die ontvangt de intents van snips) (run: sam watch, andere terminal run: rpi/voice/wheelie/index.js en dan heel hard hopen dat het t doet.</il>
</ul>
</html>
