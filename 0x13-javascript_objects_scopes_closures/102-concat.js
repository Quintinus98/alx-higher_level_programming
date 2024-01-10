#!/usr/bin/node
const fs = require('fs');

const readfile1 = fs.readFileSync(process.argv[2], 'utf-8');
const readfile2 = fs.readFileSync(process.argv[3], 'utf-8');

fs.writeFileSync(process.argv[4], readfile1 + readfile2);
