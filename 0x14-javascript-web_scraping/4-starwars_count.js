#!/usr/bin/node
const request = require('request');

const movieApi = process.argv[2];

request(movieApi, (err, res, body) => {
  if (err) console.log(err);
  if (res.statusCode === 200) {
    const data = JSON.parse(body).results;
    let count = 0;
    for (const filmId in data) {
      const character = data[filmId].characters;
      for (const charId in character) {
        if (character[charId].includes('18')) { count += 1; }
      }
    }
    console.log(count);
  }
});
