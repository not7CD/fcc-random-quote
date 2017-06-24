"""Getting contets of blockquote from all the html files"""
import urllib.request
from bs4 import BeautifulSoup



def get_blockquote_from_html(quote_html):
    """Extracts all blockquotes from given file.
        Returns list."""
    soup = BeautifulSoup(quote_html, "html.parser")
    try:
        # Try get block quote
        quote = soup.blockquote.p
        # Delete all <span> tags
        for span in quote('span'):
            span.extract()
        # Find position <br/> tag
        br_tag = quote.find('br')
        br_ind = quote.contents.index(br_tag)
        # Delete </br>
        br_tag.extract()
        # Split <blockquote> contents by <br/> index
        split_quote = (quote.contents[:br_ind], quote.contents[br_ind:])
        # Return both quote and author
        return split_quote
    except AttributeError as err:
        print(err)
        # Let calling function handle it
        raise

def clean_join(soup_list):
    str_list = [str(value) for value in soup_list]
    join_str = soup_list
    try:
        join_str = ''.join(str_list)
        return join_str
    except Exception as err:
        print(err)
        raise




def main(index_html, base_url):
    """Main function"""
    # print(index_html)
    soup = BeautifulSoup(index_html, "html.parser")
    for link in soup.find_all('a'):
        try:
            html = urllib.request.urlopen(base_url + link['href']).read()
            try:
                quote, author = get_blockquote_from_html(html)
                print(clean_join(quote), clean_join(author))
            except AttributeError as err:
                print(err)
        except urllib.error.HTTPError as err:
            print(err)



if __name__ == '__main__':
    URL = "http://www.diveintopython3.net/"
    HTML = urllib.request.urlopen(URL).read()
    main(HTML, URL)
