#!/usr/bin/bin/node
module.exports = class Square extends require('./5-square.js') {
  charPrint (a) {
    if (a === undefined) {
      this.print();
    } else {
      for (let b = 0; b < this.height; b++) console.log(a.repeat(this.width));
    }
  }
};
