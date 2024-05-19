from preprocessing import Tokenization

from abc import ABC, abstractmethod


class InformationRetrieval(ABC):
    @abstractmethod
    def get_relevant_doc_indices(query: str, inv_index: dict):
        """
        Нахождение индексов релевантных документов по запросу
        """
        tokenized_query = Tokenization.tokenize_text(query)
        relevant_indices = set()
        for token in tokenized_query:
            relevant_indices.update(inv_index[token])        
        return relevant_indices
