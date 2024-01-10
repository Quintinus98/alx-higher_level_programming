#!/usr/bin/node

const { dict } = require('./101-data');

const result = {};
console.log(dict);

for (const key in dict) {
  const newKey = dict[key];
  if (newKey in result) continue;
  result[newKey] = [];
  for (const keys in dict) {
    if (dict[keys] === newKey) {
      result[newKey].push(keys);
    }
  }
}
console.log(result);
