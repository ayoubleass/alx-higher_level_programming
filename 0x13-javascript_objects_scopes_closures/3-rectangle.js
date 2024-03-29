#!/usr/bin/node

module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let rectangle = '';
    for (let i = 0; i < this.height; i++) {
      if (i > 0) {
        rectangle += '\n';
      }
      for (let j = 0; j < this.width; j++) {
        rectangle += 'X';
      }
    }
    console.log(rectangle);
  }
};
