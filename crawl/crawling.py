import scrapy
from urllib.parse import urlencode
import pandas as pd
from scrapy.crawler import CrawlerProcess
from scrapy.linkextractors import LinkExtractor
from scrapy.signalmanager import dispatcher
from scrapy.utils.project import get_project_settings
from twisted.internet import reactor, defer
from scrapy import signals
import os
import re
import pickle
import json
import requests

class SiteCrawler:
    '''
    Класс, который содержит в себе весь функционал
    '''
    #Словари для запомниания уникальных статистических данных, используются как атрибуты класса, а не экземпляров
    unique_docs = dict()
    unique_pdfs = dict()
    unique_docxs = dict()
    unique_subdomains = dict()
    unique_broken = dict()
    #Конструктор класса
    def __init__(self, names, allowed_domains, start_urls):
        '''
        Конструктор класса SiteCrawler, получает на вход:
        names: list[str]
        allowed_domains: list[list[str]]
        start_urls: list[list[str]]
        '''
        self.names = names
        self.all_allowed_domains = allowed_domains
        self.all_start_urls = start_urls
        for name in self.names:
            SiteCrawler.unique_docs[name] = set()
            SiteCrawler.unique_docxs[name] = set()
            SiteCrawler.unique_pdfs[name] = set()
            SiteCrawler.unique_broken[name] = set()
            SiteCrawler.unique_subdomains[name] = set()
            

    def make_Spider(self, input_name, input_allowed_domains, input_start_urls):
        '''
        make_Spider - функция для создания класса наследника Spider, который будет использоваться для кроулинга
        '''
        class BasicSpider(scrapy.Spider):
            #обязательные переменные
            name = input_name
            allowed_domains = input_allowed_domains
            start_urls = input_start_urls

            def __init__(self):
                self.link_extractor = LinkExtractor()#объект, который парсит все ссылки со страницы
                self.template = re.compile(r'\S*' + self.allowed_domains[0])#шаблон регулярного выражения для поиска поддомена

            #обязательная для парсинга функция
            def parse(self, response):
                #проверка ссылки на то, является ли она документом
                isdocx = (response.url[-4:] == 'docx')
                isdoc = (response.url[-3:] == 'doc')
                ispdf = (response.url[-3:] == 'pdf')
                #по умолчанию не базовый домен
                subdomain = 'not_base_domen'
                #если ссылка документ, добавляем в соответсвующее множество в словаре
                if isdocx:
                    SiteCrawler.unique_docxs[self.name].add(response.url)
                if isdoc:
                    SiteCrawler.unique_docs[self.name].add(response.url)
                if ispdf:
                    SiteCrawler.unique_pdfs[self.name].add(response.url)
                #поддомен
                if match_result := re.match(self.template, response.url):
                        subdomain = match_result.group(0)
                        SiteCrawler.unique_subdomains[self.name].add(subdomain)
                #если ссылка документ, то не парсим, а возвращаем результат
                if isdocx or isdoc or ispdf:
                    yield{
                        'url': response.url,
                        'title': '',
                        'links': [],
                        'isdocx': isdocx,
                        'isdoc': isdoc,
                        'ispdf': ispdf,
                        'subdomain': subdomain
                    }
                #проверка ссылка на 'рабочесть'
                elif requests.get(response.url).status_code != 200:
                    SiteCrawler.unique_broken[self.name].add(response.url)
                    yield{
                        'url': response.url,
                        'title': '',
                        'links': [],
                        'isdocx': isdocx,
                        'isdoc': isdoc,
                        'ispdf': ispdf,
                        'subdomain': subdomain
                    }
                #если все ок, запоминаем информацию, и идем дальше по ссылкам
                else:
                    links = self.link_extractor.extract_links(response)
                    links = list(map(lambda x: x.url, links))
                    curr_title = response.xpath('//title/text()').extract()
                    yield{
                        'url': response.url,
                        'title': curr_title,
                        'links': links,
                        'isdocx': isdocx,
                        'isdoc': isdoc,
                        'ispdf': ispdf,
                        'subdomain': subdomain
                    }
                    if links:
                        for link in links:
                            yield scrapy.Request(response.urljoin(link))
        return BasicSpider

    def crawling(self, spiders, save_paths, names):
        '''
        Функция, которая реализует сам обход
        spiders - список наследников scrapy.Spider
        save_paths - пути для сохранения
        names - имена
        '''
        #установка нужных настроек кроулеров, для каждого из сайтов отдельно
        processes = []
        for i in range(len(names)):
            settings = {
                'BOT_NAME': names[i],
                'FEED_FORMAT' : 'csv',
                'FEED_URI': save_paths[i],
                'ROBOTSTXT_OBEY': False,
                'DOWNLOADER_MIDDLEWARES': {
        'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
        'scrapy.downloadermiddlewares.retry.RetryMiddleware': None,
        'scrapy_fake_useragent.middleware.RandomUserAgentMiddleware': 400,
        'scrapy_fake_useragent.middleware.RetryUserAgentMiddleware': 401,},
            }
            processes.append(CrawlerProcess(settings))
        # ут сам процесс
            
        @defer.inlineCallbacks
        def crawl():
            for i in range(len(processes)):
                yield processes[i].crawl(spiders[i])
            reactor.stop()
        
        crawl()
        reactor.run()
        return
    
    def crawl_all_sites(self):
        '''
        Функция, которая проходится по всем заданным в объекте класса сайтам
        '''
        spiders = []
        save_paths = []

        for i in range(len(self.names)):
            #создаем папку для сохранения всех данных и сохраняем
            if not os.path.isdir(self.names[i]):
                os.mkdir(self.names[i])
            save_paths.append(self.names[i] + '//' + 'results.csv')
            spiders.append(self.make_Spider(self.names[i], self.all_allowed_domains[i], self.all_start_urls[i]))
        
        #запускаем общий процесс обхода
        self.crawling(spiders, save_paths, self.names)

        #сохраняем данные по всем сайтам в соотвествующих папках
        for i in range(len(self.names)):
            stats = {
                    'num of docxs': len(SiteCrawler.unique_docxs[self.names[i]]),
                    'num of docs': len(SiteCrawler.unique_docs[self.names[i]]),
                    'num of pdfs': len(SiteCrawler.unique_pdfs[self.names[i]]),
                    'num of subdomains': len(SiteCrawler.unique_subdomains[self.names[i]]),
                    'num of broken urls': len(SiteCrawler.unique_broken[self.names[i]]),
                    }
            with open(self.names[i] + '//' + 'stats.json', 'w') as f:
                json.dump(stats, f)
            with open(self.names[i] + '//' + 'docxs.pickle', 'wb') as f:
                pickle.dump(SiteCrawler.unique_docxs[self.names[i]], f)
            with open(self.names[i] + '//' + 'docs.pickle', 'wb') as f:
                pickle.dump(SiteCrawler.unique_docs[self.names[i]], f)
            with open(self.names[i] + '//' + 'pdfs.pickle', 'wb') as f:
                pickle.dump(SiteCrawler.unique_pdfs[self.names[i]], f)
            with open(self.names[i] + '//' + 'broken.pickle', 'wb') as f:
                pickle.dump(SiteCrawler.unique_broken[self.names[i]], f)
            with open(self.names[i] + '//' + 'subdomains.pickle', 'wb') as f:
                pickle.dump(SiteCrawler.unique_subdomains[self.names[i]], f)
            
            


































def crawl_domen(names=['basic'], domains=[[]], start=[[]]):
    for spider_index in len(names):

        data_url = f'{names[spider_index]}'
        os.mkdir(data_url)
        unique_docs = set()
        unique_pdfs = set()
        unique_docxs = set()
        unique_subdomains = set()
        unique_broken = set()
        template = re.compile(r'/S' + repr(domains[spider_index]))
        class BasicSpider(scrapy.Spider):
        
            def __init__(self, name, domain, start):
                self.link_extractor = LinkExtractor()
                self.name = name
                self.allowed_domains = domain
                self.start_urls = start

            def parse(self, response):
                if match_result := re.match(template, response.url):
                    unique_subdomains.add(match_result.group(0))
                request_response = requests.get(response.url)

                if request_response.status_code != 200:
                    unique_broken.add(response.url)

                elif response.url[-4:] == 'docx':
                    unique_docxs.add(response.url)

                elif response.url[-3:] == 'doc':
                    unique_docs.add(response.url)

                elif response.url[-3:] =='pdf':
                    unique_pdfs.add(response.url)

                else:
                    links = self.link_extractor.extract_links(response)
                    links = list(map(lambda x: x.url, links))
                    curr_title = response.xpath('//title/text()').extract()
                    yield{
                        'url': response.url,
                        'title': curr_title,
                        'links': links,
                    }
                    if links:
                        for link in links:
                            yield scrapy.Request(response.urljoin(link))

        
