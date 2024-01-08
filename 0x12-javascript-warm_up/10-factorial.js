#!/usr/bin/node
const arg = process.argv;

function factorial (n) {
  if (isNaN(n) || n === 1) {
    return (1);
  }
  if (n > 1) {
    return factorial(n - 1) * n;
  }
}

const fact = factorial(parseInt(arg[2]));
console.log(fact);
