#!/usr/bin/node
// updates the text color of the <header> element to red (#FF0000)
// using document.querySelector to select the HTML tag
// using the style property to update the color
function updateHeaderColor () {
  document.querySelector('header').style.color = '#FF0000';
}
updateHeaderColor();
