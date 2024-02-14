#!/usr/bin/node
// computes the second biggest integer in the list of arguments.
// If no argument passed, print 0
// If the number of arguments is 1, print 0

const args = process.argv.slice(2); // get the arguments
if (args.length <= 1) {
  console.log(0);
} else {
  args.sort((a, b) => a - b); // sort the array in ascending order
  console.log(args[args.length - 2]);
}
