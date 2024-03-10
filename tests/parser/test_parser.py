import pytest
import docx 


from bs4 import BeautifulSoup as bs 
from parser.parser import extract_links_from_text, \
                          get_links_url,  get_text_url, \
                          get_links_docx, get_text_docx, \
                          get_links_pdf, get_text_pdf, \
                          get_links_doc, get_text_doc


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
#TODO (собираются не все ссылки с тестовой страницы)
test_get_links_url_url1 = 'https://x.ai/'
test_get_links_url_res1 = ['https://x.ai/', 'https://x.ai/', 'https://x.ai//about/', 'https://x.ai//career/', 'https://x.ai//prompt-ide/', 'https://dload-oktatas.educatio.hu/erettsegi/feladatok_2023tavasz_kozep/k_matang_23maj_fl.pdf', 'https://x.ai/model-card/', 'https://x.ai/career/', 'https://boards.greenhouse.io/xai/jobs/4101903007', 'https://x.ai/career/', 'https://grok.x.ai', 'https://x.com/xai', 'https://x.ai//legal/terms-of-service/', 'https://x.ai//legal/privacy-policy/']

@pytest.mark.parametrize("test_url, expected_result", [(test_get_links_url_url1, test_get_links_url_res1)])
def test_get_links_url(test_url, expected_result):
    assert get_links_url(test_url) == expected_result

#-----------------------------------------------------------------------------------
#TODO (нужно ли собирать код страницы или же всё таки контент?)
test_get_text_url_url1 = 'https://x.ai/'
test_get_text_url_res1 = bs(open('tests/parser/test_files/get_text_url_res1.txt', 'r'))

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

#-----------------------------------------------------------------------------------
test_docx_bad_path = 'tests/parser/test_files/test/ex.pdf'
docx_expected_exception = docx.opc.exceptions.PackageNotFoundError

@pytest.mark.parametrize("bad_test_path, expected_exception", [(test_docx_bad_path, docx_expected_exception)])
def test_get_text_docx_exception(bad_test_path, expected_exception):
    with pytest.raises(expected_exception):
        get_text_docx(bad_test_path)

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

#-----------------------------------------------------------------------------------
test_doc_bad_path = 'tests/parser/test_files/test/ex.pdf'
doc_expected_exception = docx.opc.exceptions.PackageNotFoundError

@pytest.mark.parametrize("test_path, expected_exception", [(test_doc_bad_path, doc_expected_exception)])
def test_get_text_doc_exception(bad_test_path, expected_exception):
    with pytest.raises(expected_exception):
        get_text_doc(bad_test_path)


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
