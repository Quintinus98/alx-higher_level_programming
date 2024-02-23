#!/usr/bin/node
const request = require('request');

const movieID = process.argv[2];
const movieApi = 'https://swapi-api.alx-tools.com/api/films/' + movieID;

request(movieApi, (err, res, body) => {
  if (err) console.log(err);
  if (res.statusCode === 200) {
    const filmCharacters = JSON.parse(body).characters;
    for (let i = 0; i < filmCharacters.length; i++) {
      const character = filmCharacters[i];

      request(character, (err, res, body) => {
        if (err) console.log(err);
        if (res.statusCode === 200) {
          console.log(JSON.parse(body).name);
        }
      });
    }
  }
});
