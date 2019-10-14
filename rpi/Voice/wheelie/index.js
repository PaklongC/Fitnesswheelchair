const{ withHermes} = require ('hermes-javascript')

  withHermes( hermes=>{
    const dialog = hermes.dialog()
    dialog.flow('froekoe:data_start',(msg,flow)=>{
      console.log(msg)
      flow.end()
      return "ok lets start running,      oops, start rolling data collection"
    })
  })
