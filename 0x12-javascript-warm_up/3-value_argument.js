#!/usr/bin/node

const argv = process.argv;
if (argv.length === 2) {
  console.log('No argument');
} else {
  argv.forEach((value, index) => {
    if (index === 2) {
      console.log(value);
    }
  });
}
