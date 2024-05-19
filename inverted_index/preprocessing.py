import re
import pandas as pd

from abc import ABC, abstractmethod
from nltk.corpus import stopwords
from nltk.stem.snowball import SnowballStemmer


class Tokenization(ABC):
    @abstractmethod
    def tokenize_text(text):
        """
        Очистка и токенизация текста
        """
        new_text = text.lower()
        stemmer = SnowballStemmer("russian")
        new_text = re.sub(r'\W', ' ', new_text)
        new_text = re.sub(r'\s{2,}', ' ', new_text)

        raw_tokens = [t for t in new_text.split()]
        stop_words = set(stopwords.words("russian"))

        final_tokens = []
        for t in raw_tokens:
            if len(t) > 1 and t not in stop_words:
                cleaned_word = stemmer.stem(t)
                final_tokens.append(cleaned_word)
        return final_tokens  


    def tokenize_doc_corpus(docs: pd.Series):
        """
        Очистка всего корпуса документов
        """
        tokenized_docs = []
        for doc in docs:
            tokenized_docs.append(Tokenization.tokenize_text(doc))
        return tokenized_docs


