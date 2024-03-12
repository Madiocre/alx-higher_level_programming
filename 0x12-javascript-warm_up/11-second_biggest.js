#!/usr/bin/node
function findSecondBiggest(args) {
  // Handle no arguments or single argument cases
  if (args.length <= 1) {
    return 0;
  }

  // Convert arguments to numbers
  const numbers = args.map(Number);

  // Find the largest and second largest elements
  let largest = -Infinity;
  let secondLargest = -Infinity;

  for (const num of numbers) {
    // Skip duplicates of the current largest
    if (num === largest) continue;

    // Update largest and second largest if necessary
    if (num > largest) {
      secondLargest = largest;
      largest = num;
    } else if (num > secondLargest) {
      secondLargest = num;
    }
  }

  return secondLargest;
}

const args = process.argv.slice(2); // Skip script name and path
const secondBiggest = findSecondBiggest(args);
console.log(secondBiggest);
