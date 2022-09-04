import re
from pprint import pprint

from bs4 import BeautifulSoup as BS
import requests
from fake_headers import Headers



class Scrap:
    host = 'https://habr.com'
    fakeheaders = Headers(os='win', headers=True).generate()
    KEYWORDS = ['дизайн', 'фото', 'web', 'python', 'pOstman', 'telegram','unreal Engine 4']

    def get_titles(self) -> list():
        response = requests.get(self.host + '/ru/all/', headers=self.fakeheaders)
        soup = BS(response.text, features='html.parser')
        articles = soup.find_all('article')
        for article in articles:
            article_t = article.find(class_='tm-article-snippet__title tm-article-snippet__title_h2')
            title = article_t.find('span').text.strip()
            article_data = article.find('time').text.strip()
            article_url = self.host + article.find(class_='tm-article-snippet__title-link').attrs['href']
            for tit in self.KEYWORDS:
                if tit.lower() in title.lower().strip(''):
                    print(f'Название - {title}, время - {article_data},URL - {article_url}')

            

my_scrap = Scrap()
pprint(my_scrap.get_titles())