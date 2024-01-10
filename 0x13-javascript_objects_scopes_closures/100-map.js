#!/usr/bin/node

const { list } = require('./100-data');

console.log(list);
const mapList = list.map((elem, index) => (elem * index));
console.log(mapList);
