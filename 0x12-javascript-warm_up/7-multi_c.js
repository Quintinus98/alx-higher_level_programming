#!/usr/bin/node
const arg = process.argv;

if (isNaN(parseInt(arg[2])) || arg[2] === undefined) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < parseInt(arg[2]); i++) {
    console.log('C is fun');
  }
}
