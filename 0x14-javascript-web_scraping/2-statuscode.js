#!/usr/bin/node
// display status code of a GET request
// first argument is the URL to request (GET)
// using the module request
// format - 'code: <status code>'
// usage: ./2-statuscode.js http://www.something.com
const request = require('request');
const url = process.argv[2];
request(url, function (error, response) {
  if (error) {
    console.error('error:', error);
  }
  console.log('code:', response.statusCode);
});
