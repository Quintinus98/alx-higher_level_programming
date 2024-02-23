#!/usr/bin/node
const request = require('request');

const movieApi = process.argv[2];
const searchCharacter = 18;
let count = 0;

request(movieApi, (err, res, body) => {
  if (err) console.log(err);
  const data = JSON.parse(body);
  for (let i = 0; i < data.count; i++) {
    const characters = data.results[i].characters;
    for (let j = 0; j < characters.length; j++) {
      const id = parseInt(characters[j].match(/\d+/)[0]);
      if (id === searchCharacter) { count += 1; }
    }
  }
  console.log(count);
});
