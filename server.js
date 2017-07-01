// Load the express module
var express = require('express');

// Configure Express server
var app = express();

app.use('/', express.static(__dirname + '/'));

var port = 8080;
app.listen(port, function () {
  console.log('listening on http://localhost:' + port);
});
