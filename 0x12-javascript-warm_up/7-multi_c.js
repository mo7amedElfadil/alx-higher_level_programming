#!/usr/bin/node
// prints a string x times
// x is the first argument

const x = parseInt(process.argv[2], 10);
if (Number.isNaN(x)) console.log('Missing number of occurrences');
else {
  for (let i = 0; i < x; i++) {
    console.log('C is fun');
  }
}
