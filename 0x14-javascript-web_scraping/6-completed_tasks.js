#!/usr/bin/node
const request = require('request');

const url = process.argv[2];

request(url, (err, res, body) => {
  if (err) console.log(err);
  if (res.statusCode === 200) {
    const usersStatus = {};
    const data = JSON.parse(body);
    for (const index in data) {
      if (data[index].completed === true) {
        const key = data[index].userId;
        if (key in usersStatus) {
          usersStatus[key] += 1;
        } else {
          usersStatus[key] = 1;
        }
      }
    }
    console.log(usersStatus);
  }
});
