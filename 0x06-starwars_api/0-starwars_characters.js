#!/usr/bin node

/**
 * Retrieves Star Wars character names from a given movie.
 * @param {number} movieId - The ID of the Star Wars movie.
 * @returns {Promise<void>} - A promise that resolves with the character names.
 */
async function getStarWarFilm(movieId) {
  const res = await fetch(
    `https://swapi-api.alx-tools.com/api/films/${movieId}`
  );
  const json = await res.json();

  const charactersNamesPromises = json.characters.map((url) =>
    getCharacterName(url)
  );
  const charactersNames = await Promise.all(charactersNamesPromises);
  charactersNames.forEach((name) => {
    console.log(name);
  });
}

/**
 * Retrieves the name of a Star Wars character from a given URL.
 * @param {string} url - The URL of the Star Wars character.
 * @returns {Promise<string>} - A promise that resolves with the character name.
 */
async function getCharacterName(url) {
  const res = await fetch(url);
  const character = await res.json();

  return character.name;
}

const movieId = process.argv[2];
getStarWarFilm(movieId);
