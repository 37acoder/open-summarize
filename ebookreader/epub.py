from ebooklib import epub, ITEM_DOCUMENT
from ebookreader.abstract import Index, Ebook
from bs4 import BeautifulSoup


def extract_epub_contents(epub_file):
    book = epub.read_epub(epub_file)
    contents = {}

    for item in book.get_items():
        if item.get_type() == ITEM_DOCUMENT:
            chapter_title = item.get_name()
            chapter_content = item.get_content().decode('utf-8')
            soup = BeautifulSoup(chapter_content, 'html.parser')

            contents[chapter_title] = soup.get_text()
    return contents


class EpubBook(Ebook):
    def __init__(self, path: str) -> None:
        super().__init__()
        self.path = path

    def index(self) -> Index:
        return Index(extract_epub_contents(self.path))
    


    