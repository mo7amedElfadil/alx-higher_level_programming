#!/usr/bin/node
// fetches and prints the title of a Star Wars movie from the Star Wars API
// https://swapi-api.alx-tools.com/api/people/5/?format=json
// the name must be displayed in the HTML tag DIV#character
// You can’t use document.querySelector to select the HTML tag
// You must use the jQuery API

const url = 'https://swapi-api.alx-tools.com/api/people/5/?format=json';

$(document).ready(() => {
  $.get(url, (data, status) => {
    if (status === 'success') { $('DIV#character').text(data.name); }
  });
});
