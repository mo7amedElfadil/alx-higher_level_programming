#!/usr/bin/node
// class Rectangle that defines a rectangle
// constructor takes 2 arguments w and h
// Initialize instance attribute width with the value of w
// Initialize instance attribute height with the value of h
// If w or h are less equal to 0 then create an empty object
module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }
};
