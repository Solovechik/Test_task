import string
import requests
from bs4 import BeautifulSoup


def collect_wiki_data(url):
    data = {}  # словарь для хранения результата
    cntr = 0  # счетчик количества элементов на странице
    pointer = ''  # текущий ключ (буква для которой идёт счет на данный момент)

    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    css_selector = '#mw-pages > div > div > .mw-category-group'
    while True:
        for link in soup.select(css_selector):
            for el in list(link.stripped_strings):
                if el in index:
                    if el != pointer:  # сброс счетчика и создание нового ключа
                        cntr = 0
                        pointer = el
                        data[pointer] = 0
                elif el in string.ascii_uppercase:  # завершение при переходе на англ. названия
                    return data
                else:
                    cntr += 1
                data[pointer] = cntr
        next_page_url = soup.find_all('a', string='Следующая страница')[0].get('href')  # обработка след. страницы
        response = requests.get(f'https://ru.wikipedia.org{next_page_url}')
        soup = BeautifulSoup(response.text, 'html.parser')


index = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЭЮЯ'
wiki_url = 'https://ru.wikipedia.org/w/index.php?title=Категория%3AЖивотные_по_алфавиту'

d = collect_wiki_data(wiki_url)
[print(f'{data[0]}: {data[1]}') for data in d.items()]
