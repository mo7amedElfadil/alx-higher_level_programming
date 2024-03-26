#!/usr/bin/node
// This script prints the title of the Star Wars movie where
// the episode number matches a given integer.
// The first argument is the episode number.
// You must use the Star wars API with the endpoint
// https://swapi-api.hbtn.io/api/films/:id
// You must use the module request
// usage: ./3-starwars_title.js <episode_number>

const request = require('request');
const episodeNumber = process.argv[2];
const url = `https://swapi-api.hbtn.io/api/films/${episodeNumber}`;

request(url, function (error, response, body) {
  if (error) {
    console.error('error:', error);
  } else {
    if (response.statusCode === 200) {
      console.log(JSON.parse(body).title);
    }
  }
});
