#!/usr/bin/node
// Writes a string to a file
// The first argument is the file path
// The second argument is the string to write
// the encoding is 'utf8'
// Usage: ./1-writeme.js <file path> <string>
// If an error occurs, print the error object

// Import the filesystem module
const fs = require('fs');
// Get the file path from the command line arguments
const filePath = process.argv[2];
// Get the string input
const stringToWrite = process.argv[3];
// Open the file
// The file is read asynchronously
// The callback function is called when the file is read
// The callback function takes two arguments: error and data
// The data argument is the content of the file
fs.writeFile(filePath, stringToWrite, 'utf8', (err) => {
  if (err) {
    console.log(err);
  }
});
