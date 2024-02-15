#!/usr/bin/node
// import an array and computes a new array
// prints both arrays
// const array1 = require('./100-data').list;
// alternative way to import the array by explicitly destructuring the object
// and using the variable name list
const { list } = require('./100-data');
console.log(list);
// console.log(array1.map((value) => value * array1.indexOf(value)));
console.log(list.map((value, idx) => value * idx));
