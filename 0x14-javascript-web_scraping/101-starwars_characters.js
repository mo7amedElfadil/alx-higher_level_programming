#!/usr/bin/node
// print all characters of a Star Wars movie
// The first argument is the Movie ID - example: 3 = Return of the Jedi
// Display one character name by line
// in the same order of the list characters in the /films/ response
// You must use the Star wars API
// You must use the module request
// $ ./100-starwars_characters.js 3

const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];

// Fetch character name
// Returns a promise
// promise is resolved with the character name
// promise is rejected with an error
function fetchCharacter (characterUrl) {
  return new Promise((resolve, reject) => {
    request(characterUrl, function (error, response, body) {
      if (error) reject(error);
      else {
        if (response.statusCode === 200) resolve(JSON.parse(body).name);
        else reject(Error('Request failed with status code ' + response.statusCode));
      }
    });
  });
}

// Request characters
// Returns a promise
// promise is resolved with the list of characters
// promise is rejected with an error
function requestCharacters (url) {
  return new Promise((resolve, reject) => {
    request(url, function (error, response, body) {
      if (error) reject(error);
      else {
        if (response.statusCode === 200) {
          const characters = JSON.parse(body).characters;
          resolve(characters);
        } else {
          reject(Error('Request failed with status code ' + response.statusCode));
        }
      }
    });
  });
}

// Main function
// asyncronously request characters
// for each character fetch the name
// print the name
// catch any error
async function main () {
  try {
    const characters = await requestCharacters(url);
    for (const character of characters) {
      const name = await fetchCharacter(character);
      console.log(name);
    }
  } catch (error) {
    console.error(error);
  }
}

main();
