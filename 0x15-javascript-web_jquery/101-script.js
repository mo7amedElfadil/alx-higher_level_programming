#!/usr/bin/node
// adds, removes and clears LI elements from a list when the user clicks
// 1. When the user clicks on the tag DIV#add_item:
//      a new element is added to the list UL.my_list
// 2. When the user clicks on the tag DIV#remove_item:
//      a last element is removed to the list UL.my_list
// 3. When the user clicks on the tag DIV#clear_list:
//      all elements of the list UL.my_list are removed
// You can’t use document.querySelector to select the HTML tag
// You must use the jQuery API
// You script must work when it imported from the HEAD tag

$(document).ready(function () {
  $('DIV#add_item').click(function () {
    const item = '<li>Item</li>';
    $('UL.my_list').append(item);
  });

  $('DIV#remove_item').click(function () {
    $('UL.my_list li').last().remove();
  });

  $('DIV#clear_list').click(function () {
    $('UL.my_list').empty();
  });
});
