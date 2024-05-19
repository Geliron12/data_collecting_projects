import pandas as pd
from abc import ABC, abstractmethod

from coding import EliasCoding


class InvertedIndex(ABC):
    @abstractmethod
    def create_inverted_index(tokenized_docs: pd.Series, data_path: str) -> dict:
        """
        Построение инвертированного индекса для токенизированного корпуса документов
        """
        inverted_index = {}
        for idx, doc in enumerate(tokenized_docs):
            did = idx+1
            for token in doc:
                if token not in inverted_index:
                    inverted_index[token] = [did]
                elif inverted_index[token][-1] != did:
                    inverted_index[token].append(did)
                else:
                    continue
        return inverted_index

    @abstractmethod
    def compress_inverted_index(inv_index: dict, mode: str):
        """
        Сжатие инвертированного индекса методом Дельта или Гамма кодирования Элиаса
        Параметры
        -------------------------
            inv_index: dict
                    сжимаемый инвертированный индекс
            mode: str
                    тип сжатия ("delta" или "gamma")
        """
        if mode == "gamma":
            for term in inv_index.keys():
                compressed_posting_list = [EliasCoding.elias_gamma_encode(post) for post in inv_index[term]]
                inv_index[term] = compressed_posting_list
        else: 
            for term in inv_index.keys():
                compressed_posting_list = [EliasCoding.elias_delta_encode(post) for post in inv_index[term]]
                inv_index[term] = compressed_posting_list
        return inv_index