#!/usr/bin/node
// fetches and lists the title for all movies by using this
// URL: https://swapi-api.alx-tools.com/api/films/?format=json
// all movie titles must be list in the HTML tag UL#list_movies
// You can’t use document.querySelector to select the HTML tag
// You must use the jQuery API

const url = 'https://swapi-api.alx-tools.com/api/films/?format=json';

$(document).ready(() => {
  $.get(url, (data, status) => {
    if (status === 'success') {
      console.log(data);
      data.results.forEach((movie) => {
        $('UL#list_movies').append(`<li>${movie.title}</li>`);
      });
    }
  });
});
