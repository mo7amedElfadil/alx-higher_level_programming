#!/usr/bin/node
// prints a message if no argument is passed or prints the first argument
// to get the argv property from the process object
const { argv } = process; // object destructuring
if (!argv[2]) console.log('No argument');
else console.log(argv[2]);
