#!/usr/bin/node
// function that returns the number of occurrences in a list
exports.nbOccurences = function (list, searchElement) {
  let count = 0;
  list.forEach(function (element) {
    if (element === searchElement) {
      count++;
    }
  });
  return count;
};
