#!/usr/bin/node
// gets the contents of a webpage and stores it in a file
// usage: ./5-request_store.js http://example.com/ file.html

const request = require('request');
const fs = require('fs');
const url = process.argv[2];
const file = process.argv[3];

request(url, function (error, response, body) {
  if (error) {
    console.error('error:', error);
    process.exit(1);
  }
  if (response.statusCode === 200) {
    fs.writeFile(file, body, 'utf8', function (err) {
      if (err) {
        console.error('error:', err);
        process.exit(1);
      }
    });
  }
});
