#!/usr/bin/node
// toggles the class of the <header> element when
// the user clicks on the tag DIV#toggle_header
// The <header> element must always have one of the two classes:
// red or green. When the user clicks on the tag DIV#toggle_header,
// the class must be toggled
// You must use the jQuery API

$('DIV#toggle_header').click(function () {
  $('header').toggleClass('red green');
});
