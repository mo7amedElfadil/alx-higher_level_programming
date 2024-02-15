#!/usr/bin/node
// class square that inherits from square 5-square.js
// and prints the square using the character c
// if c is undefined, use 'X'
const SquareOld = require('./5-square');
module.exports = class Square extends SquareOld {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let i = 0; i < this.height; i++) {
      console.log(c.repeat(this.width));
    }
  }
};
