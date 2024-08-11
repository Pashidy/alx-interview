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
  printResult(casts);
});

function printResult(casts, counter = 0) {
  request(casts[counter], function (error, _, body) {
    if (error) {
      console.error(error);
      return;
    }
    console.log(JSON.parse(body).name);
    if (counter + 1 < casts.length) {
      printResult(casts, counter + 1);
    }
  });
}
