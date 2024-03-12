#!/usr/bin/node
function factorial(num) {
  if (isNaN(num) || num === 0) {
    return 1;
  }

  return num * factorial(num - 1);
}

const firstArg = Number(process.argv[2]);

const result = factorial(firstArg);
console.log(result);
