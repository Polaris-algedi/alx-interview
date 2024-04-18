#!/usr/bin/node

const request = require("request");

/**
 * Retrieves Star Wars character names from a given movie.
 * @param {number} movieId - The ID of the Star Wars movie.
 * @returns {Promise<void>} - A promise that resolves with the character names.
 */
function getStarWarFilm(movieId) {
  const filmUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

  return new Promise((resolve, reject) => {
    request(filmUrl, (error, response, body) => {
      if (error) {
        reject(error);
        return;
      }

      if (response.statusCode !== 200) {
        reject(
          `Failed to fetch film data. Status code: ${response.statusCode}`
        );
        return;
      }

      const filmData = JSON.parse(body);
      const characterURLs = filmData.characters;

      const characterNamesPromises = characterURLs.map((url) =>
        getCharacterName(url)
      );
      Promise.all(characterNamesPromises)
        .then((characterNames) => {
          characterNames.forEach((name) => console.log(name));
          resolve();
        })
        .catch((error) => reject(error));
    });
  });
}

/**
 * Retrieves the name of a Star Wars character from a given URL.
 * @param {string} url - The URL of the Star Wars character.
 * @returns {Promise<string>} - A promise that resolves with the character name.
 */
function getCharacterName(url) {
  return new Promise((resolve, reject) => {
    request(url, (error, response, body) => {
      if (error) {
        reject(error);
        return;
      }

      if (response.statusCode !== 200) {
        reject(
          `Failed to fetch character data. Status code: ${response.statusCode}`
        );
        return;
      }

      const characterData = JSON.parse(body);
      resolve(characterData.name);
    });
  });
}

const movieId = process.argv[2];
getStarWarFilm(movieId).catch((error) => console.error("Error:", error));
