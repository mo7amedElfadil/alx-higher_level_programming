#!/usr/bin/node
// prints a message to the console based on first and second command line arguments
// to get the argv property from the process object
const { argv } = process; // object destructuring
console.log(`${argv[2]} is ${argv[3]}`);
