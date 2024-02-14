#!/usr/bin/node
// add two numbers
function add (a, b) {
  console.log(parseInt(a) + parseInt(b));
}

function check (a) {
  if (Number.isNaN(a)) {
    console.log('NaN');
    return false;
  }
  return true;
}

const num1 = process.argv[2];
const num2 = process.argv[3];

if (check(num1) && check(num2)) {
  add(num1, num2);
}
