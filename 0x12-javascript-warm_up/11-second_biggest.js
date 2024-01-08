#!/usr/bin/node
const arg = process.argv;

if (arg.length <= 3) {
  console.log(0);
} else {
  const sorted = arg.slice(2).sort((a, b) => b - a);
  console.log(sorted[1]);
}
