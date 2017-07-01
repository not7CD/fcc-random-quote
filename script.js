
$(document).ready(function() {
  var json_quotes = [];
  $.getJSON( "quotes.json", function(data) {
    json_quotes = data["quotes"];
  });
  $("#getQuote").on("click", function() {
    var i = Math.floor(Math.random() * json_quotes.length);
    $("#quote").html(json_quotes[i].quote);
    $("#author").html(json_quotes[i].author);
  });
});
