
$(document).ready(function(){

    var csrfToken = $('input[name=csrfmiddlewaretoken]').val();

    someData = 1;

    var ajaxCall = $.ajax({
        context: $('#startCrawl'),
        data: someData,
        dataType: 'json',
        url: '/path/to/script'
      });
      
      ajaxCall.done(function(data) {
        alert('Bạn Vừa Ấn Nút Này');
      });
});
