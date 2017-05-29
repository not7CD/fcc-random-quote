var parsed_json_file = [{
    cite: 'http://www.diveintopython3.net/whats-new.html',
    quote: 'Isn’t this where we came in?',
    author: 'Pink Floyd, The Wall'
  },
  {
    quote: 'Certitude is not the test of certainty. We have been cocksure of many things that were not so.',
    author: 'Oliver Wendell Holmes, Jr.'
  }
];

$(document).ready(function() {
  $("#getQuote").on("click", function() {
    var i = Math.floor(Math.random() * parsed_json_file.length);
    $("#quote").html(parsed_json_file[i].quote);
    $("#author").html(parsed_json_file[i].author);
  });
});
