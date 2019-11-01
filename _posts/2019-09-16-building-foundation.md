---
layout: post
title: Building the foundation
subtitle: Preliminary Idea and Prototype
---

## 1. Brainstorming and Preliminary idea
Three distinct product directions were found after brainstorming:
- A fitness wheelchair made for the athletic tech enthusiasts,
- a 'party' wheelchair made for entertainment/entertaining a crowd, and
- a wheelchair that could tell when and which parts of the wheelchair needs to be replaced or repaired.

For this project, the first design-direction was taken. The concept was then fleshed out more to fit the market and target-group. A few assumptions were taken along the way, which should be validated (using a prototype).

## 2. Assumptions and validation
- Collecting the velocity data will be sufficient to give relevant information/motivation.<br>
- Interaction with the concept is done using voice. Hands-free control is desirable for this target-group.<br>

1. Is velocity a relevant measurement when it comes to collecting data from a training?<br>
  - <i>Getting insight into sensor-activities and measurement accuracy</i><br>
2. To what extent is voice in and output desirable when it comes to control and output?<br>  
  - <i>Getting insight into analytics</i>

## 3. (Initial) setup and architecture
The prototype will be build using a Feather (with an IMU sensor attached) and a Raspberry Pi (with a microphone and speaker attached). The first sensor will be used to validate the first assumption mentioned. The sensor (and actuator) attached to the Raspberry Pi will be used to validate the latter.<br>
Communication between the Feather and Raspberry Pi will be done using Bluetooth. The Raspberry Pi will use WiFi to get/put data onto a server. More elaborate explanation of the architecture can be seen in the visual below.<br>
To get everything ready, the Raspberry Pi needs to be initialized correctly and the feather also. The next post will be about the sensor used.
<img src="\Fitnesswheelchair\img\IOT Architecture.png" width="775">
