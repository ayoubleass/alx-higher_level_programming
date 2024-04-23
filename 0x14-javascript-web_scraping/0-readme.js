#!/usr/bin/node

const fileName = process.argv[2];
const fs = require('fs');
fs.readFile(fileName, (error, inputD) => {
  if (error) {
    console.log(error);
    return;
  }
  console.log(inputD.toString());
});
