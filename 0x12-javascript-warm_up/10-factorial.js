#!/usr/bin/node
// computes and prints a factorial

function factorial (n) {
  if (n === 0 || isNaN(n)) {
    return 1;
  }
  return n * factorial(n - 1);
}

const num = process.argv[2];
if (Number.isNaN(num)) {
  console.log(1);
} else {
  console.log(factorial(num));
}
