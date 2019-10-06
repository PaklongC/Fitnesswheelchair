<h1>Fitnesswheelchair</h1>
<h6>By Pak Long, Freek and Lorenzo</h6>
<hr>

<body>
<h3>Scope:</h3>
<H8><b>WHAT</b></H8>
<img src="Images/fitnessChair.png" width="" height="">
<br><br>

<b>WHY</b><br>
Create a wheelchair that functions as a fitness tracker for the disabled by measuring their
development and performances. The prototype serves to test the feasibility of one of the core
features of the concept.

<h8><b>HOW</b></h8><br>
<ol>
  <li>
  Testing the accelerometer and force sensor to collect meaningful data to send to the HUB.
  </li><br>
  <ul>
    <li>Getting insight into sensor-sensitivities and accurate measurements.
  </ul></li><br>
  <li>Using the data during exercise with voice control.</li><br>
  <ul>
    <li>Getting insight into the user-interaction, guided by sound.</li>
  </ul><br>
</ol>
</body>

<hr>
<h3>Sensor analysis:</h3>

<table style="width:100%">
  <tr>
    <th>Sensor Used</th>
    <th>Data collected/needed</th>
    <th>Method</th>
    <th>Pros & Cons</th>
    <th>Take-aways</th>
  </tr>
  <tr>
    <td rowspan = 2>IMU<br><img src="Images/IMU.png" width="" height=""></td>
    <td>- Acceleration --> Velocity</td>
    <td>Integral approach by calculating the sum of velocities-values between certain time-points using the acceleration.</td>
    <td><b>+ </b>Velocity is constantly being calculated<br><b>- </b>This method is very dependant on the sensitivity of the accelerometer and its (correct) calibration. Because the sum of the measured and calculated values are used, little measurement-errors will lead to bigger and bigger deviations</td>
    <td><img src="" width="" height=""></td>
  </tr>
  <tr>
    <td rowspan = 1>- Angle displacement --> Velocity</td>
    <td>'RPM-'approach by calculating the velocity using wheelchair-specific properties.</td>
    <td><b>+ </b>This method is relatively more accurate because the angle can be measured more reliably<br><b>- </b>Because (1/f=T) is used, the speed can only be calculated when the one whole rotation of the wheel is made</td>
    <td><img src=""></td>
  </tr>
  <tr>
    <td>Microphone<br><img src="Images/soundSensor.png" width="" height=""></td>
    <td>- Voice --> recogition</td>
    <td>Using the API provided by google</td>
    <td></td>
    <td><img src=""></td>
  </tr>
</table>
