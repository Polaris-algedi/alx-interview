#!/usr/bin/node

const request = require('request');
const starWarsAPI = 'https://swapi-api.alx-tools.com/api/films/';
const movieID = process.argv[2].toString();

// Function to fetch film data
function fetchFilmData (movieID) {
  return new Promise((resolve, reject) => {
    const filmUrl = `${starWarsAPI}${movieID}`;
    request(filmUrl, (error, _, body) => {
      if (error) reject(error);
      else resolve(JSON.parse(body));
    });
  });
}

// Function to fetch character data and print names recursively
function fetchAndPrintCharacters (casts, index = 0) {
  if (index < casts.length) {
    request(casts[index], (error, _, body) => {
      if (error) console.error(error);
      else {
        const character = JSON.parse(body);
        console.log(character.name);
        fetchAndPrintCharacters(casts, index + 1);
      }
    });
  }
}

// Main function to fetch film data and print characters
async function main () {
  try {
    const filmData = await fetchFilmData(movieID);
    const casts = filmData.characters;
    fetchAndPrintCharacters(casts);
  } catch (error) {
    console.error('Error:', error);
  }
}

main();
