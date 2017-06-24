"""Getting contets of blockquote from all the html files"""
from bs4 import BeautifulSoup
import urllib.request



def get_blockquote_from_html(quote_html):
    """Extracts all blockquotes from given file.
        Returns list."""
    soup = BeautifulSoup(quote_html, "html.parser")
    quote = None
    try:
        quote = soup.blockquote.p
        for span in quote('span'):
            span.extract()

        print(list(quote.contents).index ('<br/>'))

        # for i, c in enumerate(quote.contents):
            # print(i, c)
            # print(type(c.string))
        # print(quote.contents[2])
    except AttributeError as e:
        print(e)
    return quote



def main(index_html):
    """Main function"""
    # print(index_html)
    soup = BeautifulSoup(index_html, "html.parser")
    for link in soup.find_all('a'):
        try:
            HTML = urllib.request.urlopen("http://www.diveintopython3.net/" + link['href']).read()
            quote = get_blockquote_from_html(HTML)
            print(quote)
        except urllib.error.HTTPError as e:
            print(e)



if __name__ == '__main__':
    HTML = urllib.request.urlopen("http://www.diveintopython3.net/").read()
    main(HTML)
