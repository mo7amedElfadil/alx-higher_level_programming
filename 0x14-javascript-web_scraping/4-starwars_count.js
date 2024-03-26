#!/usr/bin/node
// This script prints the number of movies where the character “Wedge Antilles” is present.
const request = require('request');

request(`${process.argv[2]}`, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    if (response.statusCode !== 200) {
      process.exit(1);
    }
    const data = JSON.parse(body);
    let apps = 0;
    data.results.forEach(movie => {
      const id = 'https://swapi-api.alx-tools.com/api/people/18/';
      if (movie.characters.indexOf(id) >= 0) apps++;
    });
    console.log(apps);
  }
});
