import sys
import time
import pickle
import pandas as pd

from pympler import asizeof

def load_dataset(data_path: str):
    df = pd.read_csv(data_path, index_col=False)
    docs = df['texts'].astype("string")
    docs.replace(pd.NaT, "", inplace=True)
    return docs

import time
def get_time(func, *args, **kwargs):
    """
    Вывод времени работы функции
    """
    start = time.time()
    res = func(*args, **kwargs)
    end = time.time()
    func_time = round(end - start, 6)
    return res, func_time


def get_object_size(some_object):
    """
    Возвращает размер объекта в килобайтах
    """
    size = asizeof.asizeof(some_object) / 1024
    return size


def save_file(file, file_name):
    with open(f'data/{file_name}.pkl', 'wb') as f:
        pickle.dump(file, f)


def load_file(file_name, format="pkl"):
    with open(f'data/{file_name}.{format}', 'rb') as f:
        data = pickle.load(f)
    return data