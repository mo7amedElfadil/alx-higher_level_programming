#!/usr/bin/node
// concat two strings from 2 files given as arguments
// the output is saved in a third file given as argument
// if the number of arguments is not 5, the program exits

// import the file system module
const fs = require('fs');
// get the arguments
const { argv } = process; // object destructuring
// check the number of arguments
if (argv.length !== 5) {
  process.exit(1);
}
// write the content into the third file
fs.writeFileSync(argv[4],
  fs.readFileSync(argv[2], 'utf8') +
  fs.readFileSync(argv[3], 'utf8'));
