from ebookreader import epub


# test epub.extract_epub_contents
def test_extract_epub_contents():
    contents = epub.extract_epub_contents('./ebookreader/test.epub')
    for k, v in contents.items():
        print(len(v))


if __name__ == '__main__':
    test_extract_epub_contents()