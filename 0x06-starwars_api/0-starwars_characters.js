#!/usr/bin/node

const request = require('request');

//Get the Movie ID from the first positional argument
const movieId = process.argv[2];

// Star Wars API URL
const apiUrl = `https://swapi-api.hbtn.io/api/films/${movieId}/`;

// Make the HTTP request to the Star Wars API
request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  const filmData = JSON.parse(body);
  const characters = filmData.characters;

  //	Loop through the list of characters and make a request for each
  characters.forEach(characterUrl => {
    request(characterUrl, (error, response, body) => {
      if (error) {
        console.error(error);
        return;
      }

      const characterData = JSON.parse(body);
      console.log(characterData.name);
    });
  });
});
