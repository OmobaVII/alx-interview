#!/usr/bin/node
// Prints all character of A star wars movie

function arrange (characters, pos) {
  if (pos >= characters.length) {
    return;
  }
  request(characters[pos], function (err, response, body) {
    if (err) {
      console.error(err);
    } else {
      const actor = JSON.parse(body);
      console.log(actor.name);
      return arrange(characters, ++pos);
    }
  });
}

const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];
const request = require('request');

request(url, function (err, response, body) {
  if (err) {
    console.error(err);
  } else {
    const characters = JSON.parse(body).characters;
    arrange(characters, 0);
  }
});
