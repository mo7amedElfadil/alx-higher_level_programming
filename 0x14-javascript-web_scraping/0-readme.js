#!/usr/bin/node
// reads and prints the content of a file
// The first argument is the file path
// the encoding is 'utf8'
// Usage: ./0-readme.js <file path>
// If an error occurs, print the error object

// Import the filesystem module
const fs = require('fs');
// Get the file path from the command line arguments
const filePath = process.argv[2];
// Read the file
// The file is read asynchronously
// The callback function is called when the file is read
// The callback function takes two arguments: error and data
// The data argument is the content of the file
fs.readFile(filePath, 'utf8', (err, data) => {
  if (err) {
    console.log(err);
    return;
  }
  console.log(data);
});
