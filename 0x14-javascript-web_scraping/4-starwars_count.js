#!/usr/bin/node
const request = require('request');

const movieApi = process.argv[2];
const searchCharacter = 'https://swapi-api.alx-tools.com/api/people/18/';
let count = 0;

request(movieApi, (err, res, body) => {
  if (err) console.log(err);
  const data = JSON.parse(body);
  for (let i = 0; i < data.count; i++) {
    const characters = data.results[i].characters;
    for (let j = 0; j < characters.length; j++) {
      if (characters[j] === searchCharacter) { count += 1; }
    }
  }
  console.log(count);
});
