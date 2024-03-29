import pytest
import docx 


from bs4 import BeautifulSoup as bs 
from parser.parser import extract_links_from_text, \
                          get_links_url,  get_text_url, \
                          get_links_docx, get_text_docx, \
                          get_links_pdf, get_text_pdf, \
                          get_links_djvu, get_text_djvu, \
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
test_get_links_url_url2 = 'https://apmath.spbu.ru/fakultet/kafedry.html'
test_get_links_url_url3 = 'https://spbu.ru/'
test_get_links_url_url4 = 'https://ru.wikipedia.org/wiki/%D0%A4%D0%B0%D0%BA%D1%83%D0%BB%D1%8C%D1%82%D0%B5%D1%82_%D0%BF%D1%80%D0%B8%D0%BA%D0%BB%D0%B0%D0%B4%D0%BD%D0%BE%D0%B9_%D0%BC%D0%B0%D1%82%D0%B5%D0%BC%D0%B0%D1%82%D0%B8%D0%BA%D0%B8_%E2%80%94_%D0%BF%D1%80%D0%BE%D1%86%D0%B5%D1%81%D1%81%D0%BE%D0%B2_%D1%83%D0%BF%D1%80%D0%B0%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D1%8F_%D0%A1%D0%B0%D0%BD%D0%BA%D1%82-%D0%9F%D0%B5%D1%82%D0%B5%D1%80%D0%B1%D1%83%D1%80%D0%B3%D1%81%D0%BA%D0%BE%D0%B3%D0%BE_%D0%B3%D0%BE%D1%81%D1%83%D0%B4%D0%B0%D1%80%D1%81%D1%82%D0%B2%D0%B5%D0%BD%D0%BD%D0%BE%D0%B3%D0%BE_%D1%83%D0%BD%D0%B8%D0%B2%D0%B5%D1%80%D1%81%D0%B8%D1%82%D0%B5%D1%82%D0%B0'


test_get_links_url_res1 = ['https://x.ai//', 'https://x.ai//blog', 'https://x.ai//about', 'https://x.ai//careers', 'https://x.ai//terms-of-service', 'https://x.ai//privacy-policy', 'https://developers.x.ai', 'https://ide.x.ai', 'https://grok.x.ai']
test_get_links_url_res2 = 'https://apmath.spbu.ru/fakultet/kafedry/6-kafedra-teorii-upravleniya'
test_get_links_url_res3 = 'https://abiturient.spbu.ru'
test_get_links_url_res4 = 'https://ru.wikipedia.org//wiki/%D0%9C%D0%B5%D1%85%D0%B0%D0%BD%D0%B8%D0%BA%D0%B0'

@pytest.mark.parametrize("test_url, expected_result", [(test_get_links_url_url1, test_get_links_url_res1)])
def test_get_links_url(test_url, expected_result):
    assert get_links_url(test_url) == expected_result

@pytest.mark.parametrize("test_url, expected_result", [(test_get_links_url_url2, test_get_links_url_res2),
                                                       (test_get_links_url_url3, test_get_links_url_res3),
                                                       (test_get_links_url_url4, test_get_links_url_res4)])
def test_get_links_url(test_url, expected_result):
    assert expected_result in get_links_url(test_url)

#DOCX-----------------------------------------------------------------------------------
document_path1 = 'tests/parser/test_files/empty'
document_path2 = 'tests/parser/test_files/eng_with_spaces_and_urls'
document_path3 = 'tests/parser/test_files/eng_with_urls'
document_path4 = 'tests/parser/test_files/just_image'
document_path5 = 'tests/parser/test_files/rus'
document_path6 = 'tests/parser/test_files/rus_and_eng'
document_path7 = 'tests/parser/test_files/space_at_the_end'
document_path8 = 'tests/parser/test_files/symbols'
document_path9 = 'tests/parser/test_files/with_image'
document_path10 = 'tests/parser/test_files/with_text_image'
document_path11 = 'tests/parser/test_files/hieroglyphs'


test_get_links_docx_result1 = []
test_get_links_docx_result2 = ['https://chat.openai.com/']
test_get_links_docx_result3 = ['https://chat.openai.com/', 'https://twitter.com/home']
test_get_links_docx_result4 = []
test_get_links_docx_result5 = []
test_get_links_docx_result6 = []
test_get_links_docx_result7 = []
test_get_links_docx_result8 = []
test_get_links_docx_result9 = []
test_get_links_docx_result10 = []
test_get_links_docx_result11 = []


@pytest.mark.parametrize("test_path, expected_result", [(document_path1 + '.docx', test_get_links_docx_result1),
                                                        (document_path2 + '.docx', test_get_links_docx_result2),
                                                        (document_path3 + '.docx', test_get_links_docx_result3),
                                                        (document_path4 + '.docx', test_get_links_docx_result4),
                                                        (document_path5 + '.docx', test_get_links_docx_result5),
                                                        (document_path6 + '.docx', test_get_links_docx_result6),
                                                        (document_path7 + '.docx', test_get_links_docx_result7),
                                                        (document_path8 + '.docx', test_get_links_docx_result8),
                                                        (document_path9 + '.docx', test_get_links_docx_result9),
                                                        (document_path10 + '.docx', test_get_links_docx_result10),
                                                        (document_path11 + '.docx', test_get_links_docx_result11)]
                                                        )
                                                        
def test_get_links_docx(test_path, expected_result):
    assert get_links_docx(test_path) == expected_result

#-----------------------------------------------------------------------------------
test_get_text_docx_result1 = ''
test_get_text_docx_result2 = 'Ijree555g\n\nhttps://chat.openai.com/'
test_get_text_docx_result3 = 'Ijree555g https://chat.openai.com/ https://twitter.com/home'
test_get_text_docx_result4 = ''
test_get_text_docx_result5 = 'Мама мыла раму'
test_get_text_docx_result6 = 'Мама мыла раму ?? Who I am'
test_get_text_docx_result7 = 'Hello world!'
test_get_text_docx_result8 = '$%✊✋₽①✔✕'
test_get_text_docx_result9 = 'Python\n\nPython'
test_get_text_docx_result10 = 'Unicode\n\nUnicode'
test_get_text_docx_result11 = '﨎﨔 働'

@pytest.mark.parametrize("test_path, expected_result", [(document_path1 + '.docx', test_get_text_docx_result1),
                                                        (document_path2 + '.docx', test_get_text_docx_result2),
                                                        (document_path3 + '.docx', test_get_text_docx_result3),
                                                        (document_path4 + '.docx', test_get_text_docx_result4),
                                                        (document_path5 + '.docx', test_get_text_docx_result5),
                                                        (document_path6 + '.docx', test_get_text_docx_result6),
                                                        (document_path7 + '.docx', test_get_text_docx_result7),
                                                        (document_path8 + '.docx', test_get_text_docx_result8),
                                                        (document_path9 + '.docx', test_get_text_docx_result9),
                                                        (document_path10 + '.docx', test_get_text_docx_result10),
                                                        (document_path11 + '.docx', test_get_text_docx_result11)]
                                                        )
def test_get_text_docx(test_path, expected_result):
    assert get_text_docx(test_path) == expected_result

#-----------------------------------------------------------------------------------
test_docx_bad_path = document_path1 + '.pdf'
docx_expected_exception = docx.opc.exceptions.PackageNotFoundError

@pytest.mark.parametrize("bad_test_path, expected_exception", [(test_docx_bad_path, docx_expected_exception)])
def test_get_text_docx_exception(bad_test_path, expected_exception):
    with pytest.raises(expected_exception):
        get_text_docx(bad_test_path)


#DOC-----------------------------------------------------------------------------------
test_get_links_doc_result1 = []
test_get_links_doc_result2 = ['https://chat.openai.com/']
test_get_links_doc_result3 = ['https://chat.openai.com/', 'https://twitter.com/home']
test_get_links_doc_result4 = []
test_get_links_doc_result5 = []
test_get_links_doc_result6 = []
test_get_links_doc_result7 = []
test_get_links_doc_result8 = []
test_get_links_doc_result9 = []
test_get_links_doc_result10 = []
test_get_links_doc_result11 = []

@pytest.mark.parametrize("test_path, expected_result", [(document_path1 + '.doc', test_get_links_doc_result1),
                                                        (document_path2 + '.doc', test_get_links_doc_result2),
                                                        (document_path3 + '.doc', test_get_links_doc_result3),
                                                        (document_path4 + '.doc', test_get_links_doc_result4),
                                                        (document_path5 + '.doc', test_get_links_doc_result5),
                                                        (document_path6 + '.doc', test_get_links_doc_result6),
                                                        (document_path7 + '.doc', test_get_links_doc_result7),
                                                        (document_path8 + '.doc', test_get_links_doc_result8),
                                                        (document_path9 + '.doc', test_get_links_doc_result9),
                                                        (document_path10 + '.doc', test_get_links_doc_result10),
                                                        (document_path11 + '.doc', test_get_links_doc_result11)]
                                                        )
def test_get_links_doc(test_path, expected_result):
    assert get_links_doc(test_path) == expected_result

#-----------------------------------------------------------------------------------
test_get_text_doc_result1 = ''
test_get_text_doc_result2 = 'Ijree555g\n\nhttps://chat.openai.com/'
test_get_text_doc_result3 = 'Ijree555g https://chat.openai.com/ https://twitter.com/home'
test_get_text_doc_result4 = ''
test_get_text_doc_result5 = 'Мама мыла раму'
test_get_text_doc_result6 = 'Мама мыла раму ?? Who I am'
test_get_text_doc_result7 = 'Hello world!'
test_get_text_doc_result8 = '$%✊✋₽①✔✕'
test_get_text_doc_result9 = 'Python\n\nPython'
test_get_text_doc_result10 = 'Unicode\n\nUnicode'
test_get_text_doc_result11 = '﨎﨔 働'


@pytest.mark.parametrize("test_path, expected_result", [(document_path1 + '.doc', test_get_text_doc_result1),
                                                        (document_path2 + '.doc', test_get_text_doc_result2),
                                                        (document_path3 + '.doc', test_get_text_doc_result3),
                                                        (document_path4 + '.doc', test_get_text_doc_result4),
                                                        (document_path5 + '.doc', test_get_text_doc_result5),
                                                        (document_path6 + '.doc', test_get_text_doc_result6),
                                                        (document_path7 + '.doc', test_get_text_doc_result7),
                                                        (document_path8 + '.doc', test_get_text_doc_result8),
                                                        (document_path9 + '.doc', test_get_text_doc_result9),
                                                        (document_path10 + '.doc', test_get_text_doc_result10),
                                                        (document_path11 + '.doc', test_get_text_doc_result11)]
                                                        )
def test_get_text_doc(test_path, expected_result):
    assert get_text_doc(test_path) == expected_result

#-----------------------------------------------------------------------------------
test_doc_bad_path = document_path1 + '.pdf'
doc_expected_exception = docx.opc.exceptions.PackageNotFoundError

@pytest.mark.parametrize("bad_test_path, expected_exception", [(test_doc_bad_path, doc_expected_exception)])
def test_get_text_doc_exception(bad_test_path, expected_exception):
    with pytest.raises(expected_exception):
        get_text_doc(bad_test_path)


#PDF-----------------------------------------------------------------------------------
test_get_links_pdf_result1 = []
test_get_links_pdf_result2 = ['https://chat.openai.com/']
test_get_links_pdf_result3 = ['https://chat.openai.com/', 'https://twitter.com/home']
test_get_links_pdf_result4 = []
test_get_links_pdf_result5 = []
test_get_links_pdf_result6 = []
test_get_links_pdf_result7 = []
test_get_links_pdf_result8 = []
test_get_links_pdf_result9 = []
test_get_links_pdf_result10 = []
test_get_links_pdf_result11 = []

@pytest.mark.parametrize("test_path, expected_result", [(document_path1 + '.pdf', test_get_links_pdf_result1),
                                                        (document_path2 + '.pdf', test_get_links_pdf_result2),
                                                        (document_path3 + '.pdf', test_get_links_pdf_result3),
                                                        (document_path4 + '.pdf', test_get_links_pdf_result4),
                                                        (document_path5 + '.pdf', test_get_links_pdf_result5),
                                                        (document_path6 + '.pdf', test_get_links_pdf_result6),
                                                        (document_path7 + '.pdf', test_get_links_pdf_result7),
                                                        (document_path8 + '.pdf', test_get_links_pdf_result8),
                                                        (document_path9 + '.pdf', test_get_links_pdf_result9),
                                                        (document_path10 + '.pdf', test_get_links_pdf_result10),
                                                        (document_path11 + '.pdf', test_get_links_pdf_result11)]
                                                        )
def test_get_links_pdf(test_path, expected_result):
    assert get_links_pdf(test_path) == expected_result

#-----------------------------------------------------------------------------------
test_get_text_pdf_result1 = ''
test_get_text_pdf_result2 = 'Ijree555g\n\nhttps://chat.openai.com/'
test_get_text_pdf_result3 = 'Ijree555g https://chat.openai.com/ https://twitter.com/home'
test_get_text_pdf_result4 = ''
test_get_text_pdf_result5 = 'Мама мыла раму'
test_get_text_pdf_result6 = 'Мама мыла раму ?? Who I am'
test_get_text_pdf_result7 = 'Hello world!'
test_get_text_pdf_result8 = '$%✊✋₽①✔✕'
test_get_text_pdf_result9 = 'Python\n\nPython'
test_get_text_pdf_result10 = 'Unicode\n\nUnicode'
test_get_text_pdf_result11 = '﨎﨔 働'

@pytest.mark.parametrize("test_path, expected_result", [(document_path1 + '.pdf', test_get_text_pdf_result1),
                                                        (document_path2 + '.pdf', test_get_text_pdf_result2),
                                                        (document_path3 + '.pdf', test_get_text_pdf_result3),
                                                        (document_path4 + '.pdf', test_get_text_pdf_result4),
                                                        (document_path5 + '.pdf', test_get_text_pdf_result5),
                                                        (document_path6 + '.pdf', test_get_text_pdf_result6),
                                                        (document_path7 + '.pdf', test_get_text_pdf_result7),
                                                        (document_path8 + '.pdf', test_get_text_pdf_result8),
                                                        (document_path9 + '.pdf', test_get_text_pdf_result9),
                                                        (document_path10 + '.pdf', test_get_text_pdf_result10),
                                                        (document_path11 + '.pdf', test_get_text_pdf_result11)]
                                                        )
def test_get_text_pdf(test_path, expected_result):
    assert get_text_pdf(test_path) == expected_result


#DJVU-----------------------------------------------------------------------------------
test_get_links_djvu_result1 = []
test_get_links_djvu_result2 = ['https://chat.openai.com/']
test_get_links_djvu_result3 = ['https://chat.openai.com/', 'https://twitter.com/home']
test_get_links_djvu_result4 = []
test_get_links_djvu_result5 = []
test_get_links_djvu_result6 = []
test_get_links_djvu_result7 = []
test_get_links_djvu_result8 = []
test_get_links_djvu_result9 = []
test_get_links_djvu_result10 = []
test_get_links_djvu_result11 = []

@pytest.mark.parametrize("test_path, expected_result", [(document_path1 + '.djvu', test_get_links_djvu_result1),
                                                        (document_path2 + '.djvu', test_get_links_djvu_result2),
                                                        (document_path3 + '.djvu', test_get_links_djvu_result3),
                                                        (document_path4 + '.djvu', test_get_links_djvu_result4),
                                                        (document_path5 + '.djvu', test_get_links_djvu_result5),
                                                        (document_path6 + '.djvu', test_get_links_djvu_result6),
                                                        (document_path7 + '.djvu', test_get_links_djvu_result7),
                                                        (document_path8 + '.djvu', test_get_links_djvu_result8),
                                                        (document_path9 + '.djvu', test_get_links_djvu_result9),
                                                        (document_path10 + '.djvu', test_get_links_djvu_result10),
                                                        (document_path11 + '.djvu', test_get_links_djvu_result11)]
                                                        )
def test_get_links_djvu(test_path, expected_result):
    assert get_links_djvu(test_path) == expected_result

#-----------------------------------------------------------------------------------
test_get_text_djvu_result1 = ''
test_get_text_djvu_result2 = 'Ijree555g\n\nhttps://chat.openai.com/'
test_get_text_djvu_result3 = 'Ijree555g https://chat.openai.com/ https://twitter.com/home'
test_get_text_djvu_result4 = ''
test_get_text_djvu_result5 = 'Мама мыла раму'
test_get_text_djvu_result6 = 'Мама мыла раму ?? Who I am'
test_get_text_djvu_result7 = 'Hello world!'
test_get_text_djvu_result8 = '$%✊✋₽①✔✕'
test_get_text_djvu_result9 = 'Python\n\nPython'
test_get_text_djvu_result10 = 'Unicode\n\nUnicode'
test_get_text_djvu_result11 = '﨎﨔 働'

@pytest.mark.parametrize("test_path, expected_result", [(document_path1 + '.djvu', test_get_text_djvu_result1),
                                                        (document_path2 + '.djvu', test_get_text_djvu_result2),
                                                        (document_path3 + '.djvu', test_get_text_djvu_result3),
                                                        (document_path4 + '.djvu', test_get_text_djvu_result4),
                                                        (document_path5 + '.djvu', test_get_text_djvu_result5),
                                                        (document_path6 + '.djvu', test_get_text_djvu_result6),
                                                        (document_path7 + '.djvu', test_get_text_djvu_result7),
                                                        (document_path8 + '.djvu', test_get_text_djvu_result8),
                                                        (document_path9 + '.djvu', test_get_text_djvu_result9),
                                                        (document_path10 + '.djvu', test_get_text_djvu_result10),
                                                        (document_path11 + '.djvu', test_get_text_djvu_result11)]
                                                        )
def test_get_text_djvu(test_path, expected_result):
    assert get_text_djvu(test_path) == expected_result
