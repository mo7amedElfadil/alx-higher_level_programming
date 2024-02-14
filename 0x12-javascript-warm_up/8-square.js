#!/usr/bin/node
// prints a square
// x is the first argument

const x = parseInt(process.argv[2], 10);
if (Number.isNaN(x)) console.log('Missing size');
else {
  for (let i = 0; i < x; i++) console.log('X'.repeat(x));
}
