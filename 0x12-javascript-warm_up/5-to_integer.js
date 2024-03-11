#!/usr/bin/node

const argv = process.argv;
const errorMessage = 'Not a number';
if (argv.length === 2) {
  console.log(errorMessage);
} else {
  if (!isNaN(parseInt(argv[2]))) {
    console.log(parseInt(argv[2]));
  } else {
    console.log(errorMessage);
  }
}
