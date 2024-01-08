#!/usr/bin/node
const arg = process.argv;

function add (a, b) {
  return a + b;
}

const sum = add(parseInt(arg[2]), parseInt(arg[3]));
console.log(sum);
