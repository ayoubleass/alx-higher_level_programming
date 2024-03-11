#!/usr/bin/node

const argv = process.argv;
if (argv.length === 2) {
  console.log('undefined is undefined');
} else {
  let output = '';
  for (let i = 0; i < argv.length; i++) {
    if (i === 2) {
      output += argv[i] + ' is ';
    }
    if (i === 3 && argv[i]) {
      output += argv[i];
    }
  }
  if (argv.length === 3) {
    output += 'undefined';
  }
  console.log(output);
}
