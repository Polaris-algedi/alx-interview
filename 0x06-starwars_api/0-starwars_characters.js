#!/usr/bin/node

const req = require('request');

req(
  `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`,
  async (err, res, body) => {
    if (!err && res.statusCode === 200) {
      const chars = JSON.parse(body).characters;
      chars.forEach(async (char) => {
        const promise = new Promise((resolve, reject) => {
          req(char, function (err, res, body) {
            if (err) {
              reject(err);
            } else {
              resolve(JSON.parse(body).name);
            }
          });
        });
        console.log(await promise);
      });
    }
  }
);
