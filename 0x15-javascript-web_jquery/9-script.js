#!/usr/bin/node
// fetches from https://fourtonfish.com/hellosalut/?lang=fr
// displays the value of hello from that fetch
// in the HTML’s tag DIV#hello
// translation of “Hello” must be displayed in the HTML tag DIV#hello
// must work when it is imported from the HEAD tag
// must use the jQuery API

const url = 'https://hellosalut.stefanbohacek.dev/?lang=fr';

$(document).ready(() => {
  $.get(url, (data, status) => {
    if (status === 'success') {
      $('DIV#hello').text(data.hello);
    }
  });
});
