#!/usr/bin/node

const num = parseInt(process.argv[2]);
let square = '';

if (isNaN(num)) {
  console.log('Missing size');
}
if (num > 0) {
  for (let i = 0; i < num; i++) {
    let j = 0;
    while (j < num) {
      square += '#';
      j++;
    }
    if (i !== num - 1) {
      square += '\n';
    }
  }
  console.log(square);
}
