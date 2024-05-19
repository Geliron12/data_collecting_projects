import sys
import time
import pickle
import pandas as pd

def load_data(data_path: str):
    df = pd.read_csv(data_path, index_col=False)
    docs = df['texts'].astype("string")
    docs.replace(pd.NaT, "", inplace=True)
    return docs

def get_time(func, *args):
    """
    Вывод времени работы функции
    """
    start = time.time()
    func(*args)
    end = time.time()
    result = round(end - start, 5)
    print(result, "cекунд.")


def get_object_size(object):
    """
    Возвращает размер объекта в килобайтах
    """
    size = sys.getsizeof(object) / 1024
    return size

def save_file(file, file_name):
    with open(f'data/{file_name}.pkl', 'wb') as f:
        pickle.dump(file, f)