from pprint import pprint
import datetime 

from bs4 import BeautifulSoup as BS
import requests
from fake_headers import Headers



host = 'https://habr.com'
url = 'https://habr.com/ru/all/'
fakeheaders = Headers(os='win', headers=True).generate()
keywords = ['дизайн', 'DoubleSubs',  'python', 'pOstman', 'telegram','Select2', 'КПК']
log_path = 'my_logs.log'

def decor_for_decor(log_path):
    def my_decor(func): 
        def wrap(*args):
            func_name = func.__name__
            print(f'Функция {func_name}')
            print(f'Парсим {url}')
            print('Переданные аргументы:', args)
            time_start = datetime.datetime.now()
            print(f'Дата и время вызова парсера: {time_start}') 
            res = func(*args)
            func_time = datetime.datetime.now() - time_start
            print(f'Время работы парсера: {func_time}')
            with open(log_path, 'a', encoding='utf-8') as f:
                f.write(f'''Function name : {func_name} Date_time: {time_start} Url: {url} ARG': {args} 'time_work': {func_time} 'result': {res}\n''')
            return res        
        return wrap
    return my_decor

@decor_for_decor(log_path)
def get_titles_and_url(url, keywords, headers) -> dict():
    result_dict = dict()
    info_list = list()
    response = requests.get(url, headers=headers)
    soup = BS(response.text, features='html.parser')
    articles = soup.find_all('article')
    for article in articles:
        article_t = article.find(class_='tm-article-snippet__title tm-article-snippet__title_h2')
        title = article_t.find('span').text.strip()
        article_data = article.find('time').text.strip()
        article_url = host + article.find(class_='tm-article-snippet__title-link').attrs['href']
        for tit in keywords:
            if tit.lower() in title.lower().strip(''):
                info_list.append(article_data)
                info_list.append(article_url)
                result_dict.update({title: info_list})
                info_list = []
    return result_dict


print(get_titles_and_url(url, keywords, fakeheaders))