#!/usr/bin/node

const args = process.argv.slice(2);
const numbers = args.map(Number);

function partition (low, high) {
  const pivot = numbers[high];
  let i = low - 1;
  let temp;
  for (let j = low; j < high; j++) {
    if (numbers[j] <= pivot) {
      i++;
      temp = numbers[j];
      numbers[j] = numbers[i];
      numbers[i] = temp;
    }
  }
  temp = numbers[i + 1];
  numbers[i + 1] = numbers[high];
  numbers[high] = temp;
  return i + 1;
}

function quickSort (low, high) {
  if (low < high) {
    const position = partition(low, high);
    quickSort(low, position - 1);
    quickSort(position + 1, high);
  }
}

quickSort(0, numbers.length - 1);
console.log(numbers[numbers.length - 2]);
