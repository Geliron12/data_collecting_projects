from parser.parser import extract_links_from_text, \
                          get_links_url,  get_text_url, \
                          get_links_docx, get_text_docx, \
                          get_links_doc, get_text_doc, \
                          get_links_pdf, get_text_pdf


def test_extract_links_from_text():
    test_text1 = 'bla blahttps://github.com/Geliron12/data_collecting_projects bla'
    test_urls1 = ['https://github.com/Geliron12/data_collecting_projects']
    assert extract_links_from_text(test_text1) == test_urls1
    
    test_text2 = 'asdfhttps://github.com/Geliron12/data_collecting_projects mda https://github.com/alexmk7/python-2023/tree/main/examples/python_tools asdf'
    test_urls2 = ['https://github.com/Geliron12/data_collecting_projects', 'https://github.com/alexmk7/python-2023/tree/main/examples/python_tools']
    assert extract_links_from_text(test_text2) == test_urls2

# def test_get_links_url():
#     test_url = 'https://guestbook.spbu.ru/upravleniya/orgupravlenie/19997-o-vozmozhnosti-polucheniya-arkhivnykh-dokumentov-2.html'
#     assert get_links_url(test_url)


# def test_get_text_url():
#     test_url = 'https://guestbook.spbu.ru/upravleniya/orgupravlenie/19997-o-vozmozhnosti-polucheniya-arkhivnykh-dokumentov-2.html'
#     assert get_text_url(test_url)



def test_get_links_docx():
    test_path = 'tests/parser/test_files/ex.docx'
    test_links = ['https://twitter.com/home', 'https://twitter.com/home', 'https://chat.openai.com/']
    assert get_links_docx(test_path) == test_links


def test_get_text_docx():
    test_path = 'tests/parser/test_files/ex2.docx'
    test_text = 'Ijree555g\nFgffop\n\nhttps://chat.openai.com/'
    assert get_text_docx(test_path) == test_text


# def test_get_links_doc():
    
#     assert get_links_doc()


# # def test_get_text_doc():
# #     assert get_text_doc()


# def test_get_links_pdf():
#     assert get_links_pdf()


# def test_get_text_pdf():
#     assert get_text_pdf()
