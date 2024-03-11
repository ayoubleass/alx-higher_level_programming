#!/usr/bin/node

const args = process.argv;
if (args[2] && args[2] > 0) {
  for (let i = 0; i < args[2]; i++) {
    console.log('C is fun');
  }
}
