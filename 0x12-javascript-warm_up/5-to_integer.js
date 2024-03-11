#!/usr/bin/node
const Arg = process.argv[2];
const num = Number(Arg);

if (!isNaN(num)) {
    console.log('My number: ' + Math.floor(num));
} else {
    console.log('Not a number');
}
