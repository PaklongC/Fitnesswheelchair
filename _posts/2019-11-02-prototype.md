---
layout: post
title: Cloud application
subtitle: Code explained
---
<html>
  <div class="row get-started-wrap">
    <img src="\Fitnesswheelchair\img\Flowchart_PCP_Jupyter.png" width="">
  </div>
</html>


### User Dashboard

  To show the data to the end-user, Jupyter Notebook is used for visual presentation in the dashboard feature. To check the full code, see the file \FINAL 1.1.ipynb. at our <a href="https://github.com/PaklongC/Fitnesswheelchair/blob/master/FINAL%201.1.ipynb">GitHub</a> (see the link in our header). The flowchart represents what happens inside the code. <br><br>
  The data that is sent from the wheelchair to the DCD HUB, has been put in a session with a specific name and indexes. To get this index information, a HTTP request is sent to the PI server via an URL. <br><br>
  Next, a connection is made the THING on our DCD HUB, to be able to collect data from the server. With the in index of the sessions on there, a start- and end-time is defined for the timeframe in which data-points are extracted into an array. <br><br>
  From this array, a .csv file is created with a name of the session. This filename is also put in a different file; Rootfile.csv. Here all the workouts are listed. This is necessary with the use of a dropdown widget to select the csv to navigate to when plotting. <br><br>
  For plotting the data from a specific csv file, the ‘selected_workout’ definition is used to in combination with the dropdown to open the rootfolder.csv and let one on the list be selected. From the workout that is selected, that has the same name as the .csv file with all the datapoints, a plot is created with the ‘dropdown_file_eventhandler’ definition. The plot is updated in the next cell. From the datafile, an average speed can be calculated too using Numpy.
