function rand_quote(quotes) {
  var i = Math.floor(Math.random() * quotes.length);
  $("#quote").html(quotes[i].quote);
  $("#author").html(quotes[i].author);
}

$(document).ready(function() {
  var json_quotes = [];
  $.getJSON( "quotes.json", function(data) {
    json_quotes = data.quotes;
    rand_quote(json_quotes);
  });

  $("#getQuote").on("click", function () {
    rand_quote(json_quotes);
  });
});
