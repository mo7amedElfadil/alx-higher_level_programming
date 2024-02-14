#!/usr/bin/node
// prints a message depending of the number of arguments passed
// to get the argv property from the process object
const { argv } = process; // object destructuring
if (argv.length === 2) console.log('No argument');
else if (argv.length === 3) console.log('Argument found');
else console.log('Arguments found');
