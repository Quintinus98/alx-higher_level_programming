$(document).ready(function () {
  $('input#btn_translate').click(function () {
    const code = $('INPUT#language_code').val();
    $.ajax({
      type: 'GET',
      url: `https://www.fourtonfish.com/hellosalut/hello/?lang=${code}`,
      success: function (data) {
        $('div#hello').text(data.hello);
      }
    });
  });
});
