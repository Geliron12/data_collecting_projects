from parser import extract_links_from_text, \
                          get_links_url,  get_text_url, \
                          get_links_docx, get_text_docx, \
                          get_links_doc, get_text_doc, \
                          get_links_pdf, get_text_pdf

#res0 = extract_links_from_text('https://github.com/alexmk7/python-2023/tree/main/examples/python_tools')
#res1 = get_links_url('https://guestbook.spbu.ru/vse-obrashcheniya.html')
#res2 = get_text_url('https://guestbook.spbu.ru/vse-obrashcheniya.html')
#test_get_links_docx = get_links_docx('tests/parser/test_files/ex.docx')
#print(test_get_links_docx)
test_get_text_docx = get_text_docx('tests/parser/test_files/ex2.docx')
print(test_get_text_docx)