from bs4 import BeautifulSoup
import urllib.request

"""Getting contets of blockquote from all the html files"""


def get_blockquote_from_file(file):
    """Extracts all blockquotes from given file.
        Returns list."""
    pass


def main(index_html):
    """Main function"""
    # print(index_html)
    soup = BeautifulSoup(index_html, "html.parser")
    for link in soup.find_all('a'):
        print(link)


if __name__ == '__main__':
    html = urllib.request.urlopen("http://www.diveintopython3.net/").read()
    main(html)
