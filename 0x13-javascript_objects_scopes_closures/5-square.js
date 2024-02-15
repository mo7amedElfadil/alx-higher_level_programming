#!/usr/bin/node
// class square that inherits from rectangle
// extends the class rectangle
// constructor that takes one argument size
// constructor called using super()

const Rectangle = require('./4-rectangle');
module.exports = class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }
};
