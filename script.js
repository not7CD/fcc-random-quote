function randomQuote(quotes) {
  var randomNumber = Math.floor(Math.random() * quotes.length);
  $("#quote").html(quotes[randomNumber].quote);
  $("#author").html(quotes[randomNumber].author);
}

$(document).ready(function() {
  var quoteArray = [];
  $.getJSON("quotes.json", function(data) {
    quoteArray = data.quotes;
    randomQuote(quoteArray);
  });

  $("#getQuote").on("click", function() {
    randomQuote(quoteArray);
  });
});
