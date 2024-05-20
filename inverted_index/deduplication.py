def deduplicate_data(docs):
    """
    Дедупликация совпадающих документов
    """
    dublication_dict = {}
    for idx, doc in enumerate(docs):
        str_doc = str(doc)
        if str_doc not in dublication_dict.keys():
            dublication_dict[str_doc] = idx
        else:
            docs[str(idx)] = dublication_dict[str_doc]
    return docs