//use hermes to subscribe to dialog mqqt
const{ withHermes} = require ('hermes-javascript')

  withHermes( hermes=>{
    //define
    const dialog = hermes.dialog()
    //subscribe to "froekoe:data_start" (snips intent from the voice platform)
    dialog.flow('froekoe:data_start',(msg,flow)=>{
      //log the message we get from the intent
      console.log(msg)
      flow.end()
      //send http request to the local piserver localhost/wheelie is the start request
      sendHttp('http://0.0.0.0:5000/wheelie');
      //return string to tell snips TTS what to say
      return "Starting"
    })
    //same for the stop intent
    dialog.flow('froekoe:data_stop',(msg,flow)=>{
      console.log(msg)
      flow.end()
      sendHttp('http://0.0.0.0:5000/stop');
      return "Stopped data collecting"
    })
  })

  //use axios to send HTTWP requests
  function sendHttp(_adress){
    //define axios
    const axios = require('axios');
    //send get HTTP request to _adress and log the response and error
    // response and console logso are optional
    // to send post request use .post
    //axios.post('http://145.94.227.95:5000/wheelie')
    axios.get(_adress)
      .then(response => {
        console.log(response);
        console.log(response.data.url);
        console.log(response.data.explanation);
      })
      .catch(error => {
        console.log(error);
      });
  }
 
