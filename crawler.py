"""Getting contets of blockquote from all the html files"""
import urllib.request
import json
from bs4 import BeautifulSoup


def get_blockquote_from_html(quote_html):
    """Extracts all blockquotes from given file.
        Returns tuple of lists."""
    soup = BeautifulSoup(quote_html, "html.parser")
    # Try get block quote
    try:
        quote = soup.blockquote.p
    except AttributeError:
        raise
    for elt in quote('span'):
        # Delete every <span> tags
        elt.extract()
    # Find position of LAST <br/> tag
    for elt in quote('br'):
        br_ind = quote.contents.index(elt)
        # Delete every <br/>
        elt.extract()
    # Split <blockquote> contents by <br/> index
    split_quote = (quote.contents[:br_ind], quote.contents[br_ind:])
    # Return both quote and author
    return split_quote


def clean_join(soup_list):
    """This function joins list to a string and cleans it from trailing whitespaces."""
    # Transform all elements to srings from bs.Tag
    str_list = [str(value) for value in soup_list]
    join_str = ''.join(str_list)
    # Clean string from whitespaces and strip em dash from the front
    return join_str.strip().lstrip('—')


def main(index_html, base_url):
    """Main function"""
    # print(index_html)
    soup = BeautifulSoup(index_html, "html.parser")
    quotes = []
    for link in soup.find_all('a'):
        try:
            # open every url in htmlwebsite (very naive method)
            html = urllib.request.urlopen(base_url + link['href']).read()
            try:
                # extract both quote and author
                quote, author = get_blockquote_from_html(html)
                # clean and append to list
                quotes.append({'quote': clean_join(quote),
                               'author': clean_join(author)})
            except AttributeError:
                pass
        except urllib.error.HTTPError:
            pass
    # Dump quotes to JSON file
    with open('quotes.json', 'w') as outfile:
        json.dump(quotes, outfile)


if __name__ == '__main__':
    URL = "http://www.diveintopython3.net/"
    HTML = urllib.request.urlopen(URL).read()
    main(HTML, URL)
