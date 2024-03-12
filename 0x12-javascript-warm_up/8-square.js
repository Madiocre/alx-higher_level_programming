#!/usr/bin/node
const firstArg = process.argv[2];

if (firstArg) {
  const size = Number(firstArg);
  // Check for NaN to ensure valid number conversion
  if (!isNaN(size)) {
    // Outer loop for rows
    for (let i = 0; i < size; i++) {
      // Inner loop for columns
      let row = '';
      for (let j = 0; j < size; j++) {
        row += 'X';
      }
      console.log(row);
    }
  } else {
    console.log('Missing size');
  }
} else {
  console.log('Missing size');
}
