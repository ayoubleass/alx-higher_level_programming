#!/usr/bin/node

const Rectangle = require('./4-rectangle');
module.exports = class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (c === undefined) {
      this.print();
    } else {
      let square = '';
      for (let i = 0; i < this.height; i++) {
        if (i > 0) {
          square += '\n';
        }
        for (let j = 0; j < this.width; j++) {
          square += c;
        }
      }
      console.log(square);
    }
  }
};
