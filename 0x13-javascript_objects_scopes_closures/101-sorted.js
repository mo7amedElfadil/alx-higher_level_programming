#!/usr/bin/node
// imports a dictionary of occurrences by user id and computes the number of occurrences by user id
const { dict } = require('./101-data.js');
const newDict = {};
for (const key in dict) {
  if (dict[key] in newDict) {
    newDict[dict[key]].push(key);
  } else {
    newDict[dict[key]] = [key];
  }
}
console.log(newDict);
