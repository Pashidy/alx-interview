#!/usr/bin/node

const request = require('request');
const starWarsAPI = 'https://swapi-api.alx-tools.com/api/';
const endPoint = 'films/';
const movieID = process.argv[2];

request(starWarsAPI + endPoint + movieID, function (error, _, body) {
  if (error) {
    console.error(error);
    return;
  }
  const objects = JSON.parse(body);
  const casts = objects.characters;
  printCharacters(casts);
});

function printCharacters(casts, index = 0) {
  if (index >= casts.length) {
    return;
  }

  request(casts[index], function (error, _, body) {
    if (error) {
      console.error(error);
      return;
    }
    console.log(JSON.parse(body).name);
    printCharacters(casts, index + 1);
  });
}
