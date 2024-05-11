import requests
import time
import random
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
import seaborn as sns

class VkParser:
    '''
    Класс, реализующий парсинг постов вк по входной строке
    '''
    def __init__(self, USER_TOKEN):
        '''Конструктор класса,
        USER_TOKEN: str - специальный токен для подключения к API
        '''
        self.USER_TOKEN = USER_TOKEN
        self.end_time = int(time.time())
        self.start_time = 1704049200
        self.data = pd.DataFrame(columns=['texts', 'likes', 'reposts', 'comments', 'user_id', 'views', 'date'])
        self.sleep_time = [0.2, 0.1, 0.3]
        self.info = dict()

    def parse_vk_weekly(self, query):
        '''
        Общая функция для парсинга всех постов по запросу query за неделю,
        возвращает статистику по итогам парсинга
        '''
        self.query = query
        while self.end_time > self.start_time:
            result = self.request_per_hour(query, self.end_time - 3600, self.end_time)
            new_df = self.get_info(result)
            self.data = pd.concat([self.data, new_df])
            self.end_time -= 3600
            time.sleep(random.choice(self.sleep_time))

        self.data.to_csv(f'{query}_{datetime.fromtimestamp(self.end_time).strftime("%Y-%m-%d")}.csv')
        self.print_info()

    def request_per_hour(self, query, start_time, end_time):
        '''
        Функция для получения записей через API
        '''
        response = requests.get('https://api.vk.com/method/newsfeed.search',
                        params={'access_token': self.USER_TOKEN,
                                'count ': 200,
                                'extended': 1,
                                'q': query,
                                'v': 5.199,
                                'start_time': start_time,
                                'end_time': end_time
                                })
        return response
        

    def get_info(self, result):
        '''
        Получаем инфофрмацию из ответа
        '''
        data = result.json()['response']['items']
        new_dict = {'texts':[], 'likes':[], 'reposts':[], 'comments':[], 'user_id':[], 'views': [], 'date' : []}
        for record in data:
            new_dict['texts'].append(record['text'])
            new_dict['likes'].append(record.get('likes', {'count': 0})['count'])
            new_dict['reposts'].append(record.get('reposts', {'count': 0})['count'])
            new_dict['comments'].append(record.get('comments', {'count': 0})['count'])
            new_dict['user_id'].append(abs(record['from_id']))
            new_dict['views'].append(record.get('views', {'count': 0})['count'])
            new_dict['date'].append(datetime.fromtimestamp(record['date']).strftime('%Y-%m-%d'))
        return pd.DataFrame(new_dict)

    def print_info(self):
        '''
        функция для вывода статистики
        '''
        if not self.info:
            self.info['Число постов'] = len(self.data)
            self.info['Суммарное число лайков'] = self.data['likes'].sum()
            self.info['Суммарное число комментариев'] = self.data['comments'].sum()
            self.info['Суммарное число репостов'] = self.data['reposts'].sum()
            self.info['Суммарное число просмотров'] = self.data['views'].sum()
            self.info['Суммарное число пользователей и групп'] = self.data['user_id'].nunique()

        print(self.info)


    def plot_stats(self):
        '''
        Функция для построения графиков
        '''
        sns.set_style("darkgrid")
        fig, ax = plt.subplots(figsize=(10,6))
        sum_data = self.data.groupby('date').sum()
        plt.locator_params(axis='x', nbins=14)
        plt.plot(self.data.groupby('date').count()['texts'], '-*', label='Количество постов')
        plt.plot(sum_data['likes'], '-*', label='Количество лайков')
        plt.plot(sum_data['reposts'], '-*', label='Количество репостов')
        plt.plot(sum_data['comments'], '-*', label='Количество комментариев')
        plt.title(f'Статистика по запросу: {self.query}')
        plt.legend()

        