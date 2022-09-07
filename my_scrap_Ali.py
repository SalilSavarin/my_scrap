from bs4 import BeautifulSoup as BS
import requests
from fake_headers import Headers



class Scrap:
    host = 'https://aliexpress.ru/'
    fakeheaders = Headers(os='mac', headers=True).generate()

    def get_html(self,params=None):# -> 'bs4.element.ResultSet'
        response = requests.get(self.host + 'category/202000104/laptops.html?g=undefined&page=1&spm=a2g2w.home.104.3.29de501dYFMV', 
        headers=self.fakeheaders)
        soup = BS(response.text, features='html.parser')
        page = soup.find_all('div', class_='product-snippet_ProductSnippet__content__1ettdy')
        for item in page:
            item_name= item.find('div',class_='product-snippet_ProductSnippet__name__1ettdy').text
            try:
                shop_name= item.find('div', class_='product-snippet_ProductSnippet__caption__1ettdy').text
                print(f'Название {item_name} Магазин {shop_name}')
            except AttributeError:
                print(f'Название {item_name} Магазина нет - РЕКЛАМА')

my_scrap = Scrap()
print(my_scrap.get_html())