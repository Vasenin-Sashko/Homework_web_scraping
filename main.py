from turtle import title
from urllib import response
import requests
import bs4

# определяем список ключевых слов
KEYWORDS = ['дизайн', 'фото', 'web', 'python']

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.5) Gecko/20091102 Firefox/3.5.5 (.NET CLR 3.5.30729)',
    'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.7',
    'Keep-Alive': '300',
    'Connection': 'keep-alive',
    'Cookie': 'PHPSESSID=r2t5uvjq435r4q7ib3vtdjq120'
    }

# Ваш код

base_url = 'https://habr.com/ru/all/'

response = requests.get(base_url, headers=HEADERS)
text = response.text

soup = bs4.BeautifulSoup(text, features='html.parser')

articles = soup.find_all('article')


for article in articles:
    heading = article.find('h2').find('a').text
    preview_text = article.find('div').text
    date = article.find('time').attrs['title']
    href = article.find(class_='tm-article-snippet__title-link').attrs['href']
    link = base_url + href
    title_article = article.find('h2').find('span').text

    for word in KEYWORDS:
        if (word.lower() in heading.lower() or word.lower() in preview_text.lower()):
            print(f'Дата: {date} - Заголовок: {title_article} - Ссылка: {link}')
