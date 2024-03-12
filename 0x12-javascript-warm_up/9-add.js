#!/usr/bin/node
function add (a, b) {
  return a + b;
}

const firstArg = Number(process.argv[2]);
const secondArg = Number(process.argv[3]);

if (!isNaN(firstArg) && !isNaN(secondArg)) {
  const sum = add(firstArg, secondArg);
  console.log(sum);
} else {
  console.log('Please provide two valid numbers');
}
