const{ withHermes} = require ('hermes-javascript')

  withHermes( hermes=>{
    const dialog = hermes.dialog()

    dialog.flow('froekoe:data_start',(msg,flow)=>{
      console.log(msg)
      flow.end()
      return "ok lets start running,      oops, start rolling data collection"
    })

    dialog.flow('froekoe:data_stop',(msg,flow)=>{
      console.log(msg)
      flow.end()
      return "Stopped data collecting,      start analysis,   you would be faster if you ran"
    })
  })

const request = require('request');

request.post('http://service.com/upload')
