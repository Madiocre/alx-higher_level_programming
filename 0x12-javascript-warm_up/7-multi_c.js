#!/usr/bin/node
const firstArg = process.argv[2];

if (firstArg) {
  const num = Number(firstArg);
  // Check for NaN to ensure valid number conversion
  if (!isNaN(num)) {
    for (let i = 0; i < num; i++) {
      console.log('C is fun');
    }
  } else {
    console.log('Missing number of occurrences');
  }
} else {
  console.log('Missing number of occurrences');
}
