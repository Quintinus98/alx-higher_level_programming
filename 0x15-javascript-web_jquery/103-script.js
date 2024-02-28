$(document).ready(function () {
  function getTranslation () {
    const code = $('INPUT#language_code').val();
    $.ajax({
      type: 'GET',
      url: `https://www.fourtonfish.com/hellosalut/hello/?lang=${code}`,
      success: function (data) {
        $('div#hello').text(data.hello);
      }
    });
  }

  $('INPUT#btn_translate').click(getTranslation);

  $('INPUT#language_code').keypress(function (event) {
    if (event.which == 13) {
      getTranslation();
    }
  });
});
