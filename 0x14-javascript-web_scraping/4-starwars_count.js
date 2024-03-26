#!/usr/bin/node
// Print the number of movies where the character “Wedge Antilles” appeared.
// The first argument is the API URL of the Star wars API:
// https://swapi-api.hbtn.io/api/films/
// Wedge Antilles is character ID 18 -
// your script must use this ID for filtering the result of the API
// You must use the module request

const request = require('request');
const url = process.argv[2];

request(url, function (error, response, body) {
  if (error) {
    console.error('error:', error);
    process.exit(1);
  }

  if (response.statusCode === 200) {
    const data = JSON.parse(body).results;
    let count = 0;
    data.forEach(movie => {
      movie.characters.forEach(url => {
        if (url.includes('18')) {
          count++;
        }
      });
    });
    console.log(count);
  }
});
