---
layout: post
title: Finalizing the prototype
subtitle: The Final Result
bigimg: /img/banner2.png
---
<html>
  <div class="row get-started-wrap">
    <img src="\Fitnesswheelchair\img\rolstoel.jpg" width="376"> <img src="\Fitnesswheelchair\img\arduinonono.jpg" width="376">
  </div>
</html>

### Research questions related to the prototype
1. Is velocity a relevant measurement when it comes to collecting data from a training?  
  - <b>The velocity is relevant, but needs to be measured accurately. differentiating the angle displacement over time seems (at least with the IMU-sensor used) to be the most dependant way of achieving this. </b><br>
2. To what extent is voice in- and output desirable when it comes to control and output?  
  - <b>Although voice input is preferable over using hands, background noise can make the input and output difficult to understand. Using haptics instead of sound might be even more preferable, but this has not been tested/validated.</b><br><br>

### Improvements
<ul>
  <li><b> Add more in depth voice control </b><br>Currently we have only limited voice control implementation and to better test this feature we need to implement more options like snips connect, disconnect, status ,set workout</li>
  <li><b>Add different workout options</b><br> Currently we only have a single workout with a set distance and speed</li>
  <li><b>Improve the interaction</b><br> Currently when we start a session we are connecting to the Bluetooth and setting everything up. After the workout we disconnect and save all the data. This means that when we start a workout we have to wait on the connecting. A better solution would be to have the connecting and disconnecting seperate from the workout start and stop</li>
  <li><b>Implement data analytics</b><br> Currently our assistant is barebones and only tells if you are on track or going to slow. Although this gives basic info it does not add much value. For visualisation we only plot a speed graph and tell the average speed. The next improvement would be to use machine learning to label your data and give appropiate feedback on your session. Like at t=5 "you started to deviate a lot try to keep it more constant or slow down a bit"  </li>
  <li><b>Add extra control</b><br>Currently we have basic mobile functionality. (we can start stop and retrieve data on your phone) but an mobile app should be added to make data visualisation easy and improve user interaction because it is nice to have two ways of interacting with your fitness assistant, either by voice or by phone </li>
</ul><br>

### Final IoT-stack
<html>
  <img src="\Fitnesswheelchair\img\IOTstack.png" width="745">
</html> 
