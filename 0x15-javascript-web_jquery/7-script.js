$(function () {
  const $character = $('div#character');

  $.ajax({
    type: 'GET',
    url: 'https://swapi-api.alx-tools.com/api/people/5/?format=json',
    success: function (info) {
      $character.text(info.name);
    }
  });
});
