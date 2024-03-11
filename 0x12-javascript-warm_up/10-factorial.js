#!/usr/bin/node

function factoriel (num) {
  if (isNaN(num) || num === 0) {
    return 1;
  }
  return num * factoriel(num - 1);
}

console.log(factoriel(parseInt(process.argv[2])));
