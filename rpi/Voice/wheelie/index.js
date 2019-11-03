const{ withHermes} = require ('hermes-javascript')

  withHermes( hermes=>{
    const dialog = hermes.dialog()

    dialog.flow('froekoe:data_start',(msg,flow)=>{
      console.log(msg)
      flow.end()
      sendHttp('http://0.0.0.0:5000/wheelie');

      return "Starting"
      //return "ok lets start running,      oops, start rolling data collection"
    })

    dialog.flow('froekoe:data_stop',(msg,flow)=>{
      console.log(msg)
      flow.end()
      sendHttp('http://0.0.0.0:5000/stop');
      return "Stopped data collecting"
    })
  })

  function sendHttp(_adress){
    const axios = require('axios');

    //axios.post('http://145.94.227.95:5000/wheelie')
    //axios.post('http://145.94.228.80:5000/wheelie')
    axios.post(_adress)
      .then(response => {
        console.log(response);
        console.log(response.data.url);
        console.log(response.data.explanation);
      })
      .catch(error => {
        console.log(error);
      });
  }
