#!/usr/bin/node
// This script prints the number of movies where the character “Wedge Antilles” is present.
const request = require('request');
const url = process.argv[2];

request(url, (error, response, body) => {
  if (error) {
    console.error('error:', error);
  } else {
    if (response.statusCode !== 200) {
      process.exit(1);
    }
    const data = JSON.parse(body);
    let apps = 0;
    const id = 'https://swapi-api.alx-tools.com/api/people/18/';
    data.results.forEach(movie => {
      if (movie.characters.includes(id)) apps++;
    });
    console.log(apps);
  }
});
