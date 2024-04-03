#!/usr/bin/node
// updates the text color of the HTML tag HEADER to red (#FF0000)
// You must use document.querySelector to select the HTML tag
// You can’t use the jQuery API
// Note: Your script must be imported from the HEAD tag, not at the end of the HTML
// set event listener on document load
document.addEventListener('DOMContentLoaded', function () {
  document.querySelector('header').style.color = '#FF0000';
});
