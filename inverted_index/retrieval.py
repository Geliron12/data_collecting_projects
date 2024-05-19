import pandas as pd

from preprocessing import Tokenization
from coding import EliasCoding

from abc import ABC, abstractmethod


class IRetrieval(ABC):
    @abstractmethod
    def get_relevant_doc_indices(query: str, inv_index: dict, compressed=""):
        """
        Нахождение индексов релевантных документов по запросу
        """
        tokenized_query = Tokenization.tokenize_text(query)
        or_relevant_indices = set()
        for token in tokenized_query:
            if token not in inv_index:
                continue
            match compressed:
                case "gamma":
                    or_relevant_indices.update(EliasCoding.decode_gamma_string(inv_index[token].to01()))
                case "delta":
                    or_relevant_indices.update(EliasCoding.decode_delta_string(inv_index[token].to01())) 
                case _:
                    or_relevant_indices.update(inv_index[token])      
        return or_relevant_indices

