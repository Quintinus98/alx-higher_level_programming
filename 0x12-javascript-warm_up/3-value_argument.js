#!/usr/bin/node
const argv = process.argv
let state = 0;

argv.forEach((val, index) => {
  if (index >= 2) {
    state = 1;
    console.log(val);
  }
});
if (state === 0) {
  console.log('No argument');
}
