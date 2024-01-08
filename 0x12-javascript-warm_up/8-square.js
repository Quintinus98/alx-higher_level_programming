#!/usr/bin/node
const arg = process.argv;

if (isNaN(parseInt(arg[2])) || arg[2] === undefined) {
  console.log('Missing size');
} else {
  const size = parseInt(arg[2]);
  for (let i = 0; i < size; i++) {
    let row = '';
    for (let j = 0; j < size; j++) {
      row += 'X';
    }
    console.log(row);
  }
}
