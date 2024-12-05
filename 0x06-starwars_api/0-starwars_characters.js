#!/usr/bin/node
"""NO imported Module"""

const request = require('request');

const movieId = process.argv[2];

const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  const movieData = JSON.parse(body);

  const characters = movieData.characters;

  const fetchCharacter = (index) => {
    if (index >= characters.length) return;

    request(characters[index], (err, res, characterBody) => {
      if (err) {
        console.error(err);
        return;
      }

      const character = JSON.parse(characterBody);
      console.log(character.name);

      fetchCharacter(index + 1);
    });
  };

  fetchCharacter(0);
});
