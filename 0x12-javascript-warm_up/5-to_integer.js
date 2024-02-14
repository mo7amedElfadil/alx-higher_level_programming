#!/usr/bin/node
// prints a number if it can be converted to an integer
// to get the argv property from the process object
const { argv } = process; // object destructuring
const n = parseInt(argv[2], 10);
if (Number.isNaN(n)) console.log('Not a number');
else console.log(`My number: ${n}`);
