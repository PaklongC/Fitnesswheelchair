const axios = require('axios');

axios.post('https://145.94.227.95:5000/wheelie')
  .then(response => {
    console.log(response);
    console.log(response.data.url);
    console.log(response.data.explanation);
  })
  .catch(error => {
    console.log(error);
  });
