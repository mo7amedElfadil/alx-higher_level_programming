#!/usr/bin/node
// fetches and prints how to say “Hello” depending of the language
// using this API: https://fourtonfish.com/hellosalut/hello/
// The language code will be the value entered in the input field
// tag: INPUT#language_code eg: en, fr, es, etc.
// tag: INPUT#btn_translate: click to translate the text
// tag: DIV#hello: where the translation of “Hello” must be displayed
// The translation must be fetched when the user clicks on the tag DIV#hello
// cant use document.querySelector to select the HTML tag
// must use the jQuery API
// must work when it is imported from the HEAD tag

$(document).ready(function () {
  // the url https://fourtonfish.com/hellosalut/hello/ doesnt work
  // const url = 'https://fourtonfish.com/hellosalut/hello/';
  // using this url instead
  // https://hellosalut.stefanbohacek.dev/
  const url = 'https://hellosalut.stefanbohacek.dev/';
  $('INPUT#btn_translate').click(function () {
    const lang = $('INPUT#language_code').val();
    $.get(url + '?lang=' + lang, function (data) {
      $('DIV#hello').text(data.hello);
    });
  });
});
