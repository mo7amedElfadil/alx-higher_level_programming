#!/usr/bin/node
// class Rectangle that defines a rectangle
// constructor takes 2 arguments w and h
// Initialize instance attribute width with the value of w
// Initialize instance attribute height with the value of h
// If w or h are less equal to 0 then create an empty object
// create an instance method called print() that prints the rectangle using the character X
// create an instance method called rotate() that exchanges the width and the height of the rectangle
// create an instance method called double() that multiples the width and the height of the rectangle by 2
module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let i;
    for (i = 0; i < this.height; i++) {
      console.log('X'.repeat(this.width));
    }
  }

  rotate () {
    [this.width, this.height] = [this.height, this.width];
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
};
