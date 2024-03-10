import pytest

from parser.parser import extract_links_from_text, \
                          get_links_url,  get_text_url, \
                          get_links_docx, get_text_docx, \
                          get_links_doc, get_text_doc, \
                          get_links_pdf, get_text_pdf


#URL-----------------------------------------------------------------------------------
test_extract_links_from_text_input1 = 'bla blahttps://github.com/Geliron12/data_collecting_projects bla'
test_extract_links_from_text_result1 = ['https://github.com/Geliron12/data_collecting_projects']
test_extract_links_from_text_input2 = 'asdfhttps://github.com/Geliron12/data_collecting_projects mda https://github.com/alexmk7/python-2023/tree/main/examples/python_tools asdf'
test_extract_links_from_text_result2 = ['https://github.com/Geliron12/data_collecting_projects', 'https://github.com/alexmk7/python-2023/tree/main/examples/python_tools']

@pytest.mark.parametrize("test_text, expected_result", [(test_extract_links_from_text_input1, test_extract_links_from_text_result1),
                                                        (test_extract_links_from_text_input2, test_extract_links_from_text_result2)])
def test_extract_links_from_text(test_text, expected_result):
    assert extract_links_from_text(test_text) == expected_result
    

#WEBSITE-----------------------------------------------------------------------------------
test_get_links_url_url1 = 'https://twitter.com/home'
test_get_links_url_res1 = ['https://help.twitter.com/using-twitter/twitter-supported-browsers', 'https://twitter.com/tos', 'https://twitter.com/privacy', 'https://support.twitter.com/articles/20170514', 'https://legal.twitter.com/imprint.html', 'https://business.twitter.com/en/help/troubleshooting/how-twitter-ads-work.html?ref=web-twc-ao-gbl-adsinfo&utm_source=twc&utm_medium=web&utm_campaign=ao&utm_content=adsinfo']

@pytest.mark.parametrize("test_url, expected_result", [(test_get_links_url_url1, test_get_links_url_res1)])
def test_get_links_url(test_url, expected_result):
    assert get_links_url(test_url) == expected_result

#-----------------------------------------------------------------------------------
test_get_text_url_url1 = 'https://twitter.com/home'
test_get_text_url_res1 = open('tests/parser/test_files/get_text_url_res1.txt', 'r')

@pytest.mark.parametrize("test_url, expected_result", [(test_get_text_url_url1, test_get_text_url_res1)])
def test_get_text_url(test_url, expected_result):
    assert get_text_url(test_url) == expected_result

#DOCX-----------------------------------------------------------------------------------
test_get_links_docx_path = 'tests/parser/test_files/ex.docx'
test_get_links_docx_result = ['https://twitter.com/home', 'https://twitter.com/home', 'https://chat.openai.com/']
test_get_links_docx_path1 = 'tests/parser/test_files/ex1.docx'
test_get_links_docx_result1 = []
test_get_links_docx_path2 = 'tests/parser/test_files/ex2.docx'
test_get_links_docx_result2 = ['https://chat.openai.com/']

@pytest.mark.parametrize("test_path, expected_result", [(test_get_links_docx_path, test_get_links_docx_result),
                                                        (test_get_links_docx_path1, test_get_links_docx_result1),
                                                        (test_get_links_docx_path2, test_get_links_docx_result2)])
def test_get_links_docx(test_path, expected_result):
    assert get_links_docx(test_path) == expected_result

#-----------------------------------------------------------------------------------
test_get_text_docx_path1 = 'tests/parser/test_files/ex1.docx'
test_get_text_docx_result1 = ''
test_get_text_docx_path2 = 'tests/parser/test_files/ex2.docx'
test_get_text_docx_result2 = 'Ijree555g\nhttps://chat.openai.com/'

@pytest.mark.parametrize("test_path, expected_result", [(test_get_text_docx_path1, test_get_text_docx_result1),
                                                        (test_get_text_docx_path2, test_get_text_docx_result2)])
def test_get_text_docx(test_path, expected_result):
    assert get_text_docx(test_path) == expected_result

#DOC-----------------------------------------------------------------------------------
test_get_links_doc_path = 'tests/parser/test_files/ex.doc'
test_get_links_doc_result = ['https://twitter.com/home', 'https://twitter.com/home', 'https://chat.openai.com/']
test_get_links_doc_path1 = 'tests/parser/test_files/ex1.doc'
test_get_links_doc_result1 = []
test_get_links_doc_path2 = 'tests/parser/test_files/ex2.doc'
test_get_links_doc_result2 = ['https://chat.openai.com/']

@pytest.mark.parametrize("test_path, expected_result", [(test_get_links_docx_path, test_get_links_docx_result),
                                                        (test_get_links_docx_path1, test_get_links_docx_result1),
                                                        (test_get_links_docx_path2, test_get_links_docx_result2)])
def test_get_links_doc(test_path, expected_result):
    assert get_links_doc(test_path) == expected_result

#-----------------------------------------------------------------------------------
test_get_text_doc_path1 = 'tests/parser/test_files/ex1.doc'
test_get_text_doc_result1 = ''
test_get_text_doc_path2 = 'tests/parser/test_files/ex2.doc'
test_get_text_doc_result2 = 'Ijree555g\nhttps://chat.openai.com/'


@pytest.mark.parametrize("test_path, expected_result", [(test_get_text_doc_path1, test_get_text_doc_result1),
                                                        (test_get_text_doc_path2, test_get_text_doc_result2)])
def test_get_text_doc(test_path, expected_result):
    assert get_text_doc(test_path) == expected_result

#PDF-----------------------------------------------------------------------------------
test_get_links_pdf_url = 'tests/parser/test_files/ex.pdf'
test_get_links_pdf_res = ['https://chat.openai.com/', 'https://twitter.com/home', 'https://twitter.com/home']
test_get_links_pdf_url1 = 'tests/parser/test_files/ex1.pdf'
test_get_links_pdf_res1 = []
test_get_links_pdf_url2 = 'tests/parser/test_files/ex2.pdf'
test_get_links_pdf_res2 = ['https://chat.openai.com/']

@pytest.mark.parametrize("test_url, expected_result", [(test_get_links_pdf_url, test_get_links_pdf_res),
                                                       (test_get_links_pdf_url1, test_get_links_pdf_res1),
                                                       (test_get_links_pdf_url2, test_get_links_pdf_res2)])
def test_get_links_pdf(test_url, expected_result):
    assert get_links_pdf(test_url) == expected_result

#-----------------------------------------------------------------------------------
test_get_text_pdf_path1 = 'tests/parser/test_files/ex1.pdf'
test_get_text_pdf_result1 = ' '
test_get_text_pdf_path2 = 'tests/parser/test_files/ex2.pdf'
test_get_text_pdf_result2 = 'Ijree555g https://chat.openai.com/ '

@pytest.mark.parametrize("test_url, expected_result", [(test_get_text_pdf_path1, test_get_text_pdf_result1),
                                                       (test_get_text_pdf_path2, test_get_text_pdf_result2)])
def test_get_text_pdf(test_url, expected_result):
    assert get_text_pdf(test_url) == expected_result
