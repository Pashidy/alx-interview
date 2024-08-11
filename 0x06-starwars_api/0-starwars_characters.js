#!/usr/bin/node

const axios = require('axios');

// Get the Movie ID from the first positional argument
const movieId = process.argv[2];

// Star Wars API URL
const apiUrl = `https://swapi-api.hbtn.io/api/films/${movieId}/`;

// Make the HTTP request to the Star Wars API
axios.get(apiUrl)
  .then(response => {
    const characters = response.data.characters;

    // Create an array of Promises for each character request
    const characterPromises = characters.map(characterUrl => {
      return axios.get(characterUrl).then(res => res.data.name);
    });

    // Resolve all Promises and print character names in order
    return Promise.all(characterPromises);
  })
  .then(names => {
    names.forEach(name => console.log(name));
  })
  .catch(error => {
    console.error(error);
  });
