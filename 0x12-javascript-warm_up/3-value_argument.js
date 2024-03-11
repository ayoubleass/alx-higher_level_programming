#!/usr/bin/node

const argv = process.argv.slice(2);
if (!argv[0]) {
  console.log('No argument');
} else {
  argv.forEach((value, index) => {
    if (index === 0) {
      console.log(value);
    }
  });
}
