import re
from bs4 import BeautifulSoup as bs 
import requests
from docx import Document as docxdoc
from docx.shared import Inches
from docx.opc.constants import RELATIONSHIP_TYPE as RT
from spire.doc import *
from spire.doc.common import *
from PyPDF2 import PdfReader

def extract_links_from_text(text):
  """Вспомогательная функция для извлечения ссылок из строкового значения"""
  url_extract_pattern = "https?:\\/\\/(?:www\\.)?[-a-zA-Z0-9@:%._\\+~#=]{1,256}\\.[a-zA-Z0-9()]{1,6}\\b(?:[-a-zA-Z0-9()@:%_\\+.~#?&\\/=]*)"
  return re.findall(url_extract_pattern, text)

def correct_url(url, found_link):
    if (found_link is None or len(found_link) == 0):
        return None
    if (found_link[0] == '/'):
        return url + found_link
    if (len(found_link) < len('https') or found_link[:len('https')] != 'https'):
        return None
    return found_link

def get_links_url(url):
    """Извлекает ссыкли из html кода веб-страницы по ее ссылке
    с помощью библиотеки beautifulsoup4
    """
    result = requests.get(url)
    page = result.text
    doc = bs(page)
    links = [correct_url(url, element.get('href')) for element in doc.find_all('a')]
    return list(filter(None, links))

def get_text_url(url):
    """Извлекает html код веб-страницы по ее ссылке
    с помощью библиотеки beautifulsoup4
    """
    result = requests.get(url)
    page = result.text
    doc = bs(page)
    return doc

def get_links_docx(file_path):
    """Получение ссылок файла с расширением docx
    с помощью библиотеки python-docx
    """
    document = docxdoc(file_path)
    rels = document.part.rels
    def iter_hyperlink_rels(rels):
        for rel in rels:
            if rels[rel].reltype == RT.HYPERLINK:
                yield rels[rel]._target
    return [now for now in iter_hyperlink_rels(rels)]

def get_text_docx(file_path):
    """Получение текста файла с расширением docx
    с помощью библиотеки python-docx
    """
    doc = docxdoc(file_path)
    fullText = []
    for para in doc.paragraphs:
        fullText.append(para.text)
    return '\n'.join(fullText)

def get_text_doc(file_path):
    """Получение текста файла с расширением .doc,
    для этого файл конвертируется с расширением docx,
    с помощью библиотеки Spire.Doc,
    далее используется функция get_text_docx
    """
    document = Document()
    document.LoadFromFile('/content/ex.doc')
    document.SaveToFile('/content/TEMP.docx', FileFormat.Docx2016)
    document.Close()
    return get_text_docx('/content/TEMP.docx')[len('Evaluation Warning: The document was created with Spire.Doc for Python.\n'):]

def get_links_doc(file_path):
    """Получение ссылок файла с расширением .doc,
    для этого получается текст файла с помощью get_text_doc,
    далее используется функция extract_links_from_text для
    извелечения ссылок из текста
    """
    return extract_links_from_text(get_text_doc(file_path))

def get_links_pdf(file_path):
    """Получение ссылок файла с расширением pdf
    с помощью библиотеки PyPDF2
    """
    ans = []
    with open(file_path, 'rb') as book:
        book_reader = PdfReader(book)
        page_list = book_reader.pages
        for i in range(len(page_list)):
            story_page = page_list[i]
            page_text = story_page.extract_text()
            url_extract_pattern = "https?:\\/\\/(?:www\\.)?[-a-zA-Z0-9@:%._\\+~#=]{1,256}\\.[a-zA-Z0-9()]{1,6}\\b(?:[-a-zA-Z0-9()@:%_\\+.~#?&\\/=]*)"
            ans += re.findall(url_extract_pattern, str(page_text))
    return ans

def get_text_pdf(file_path):
    """Получение текста файла с расширением pdf
    с помощью библиотеки PyPDF2
    """
    ans = ''
    with open(file_path, 'rb') as book:
        book_reader = PdfReader(book)
        page_list = book_reader.pages
        for i in range(len(page_list)):
            story_page = page_list[i]
            ans += story_page.extract_text()
    return ans
