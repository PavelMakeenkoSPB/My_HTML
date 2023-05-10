from bs4 import BeautifulSoup
import requests
url = 'http://mignews.com/mobile'
page = requests.get(url)
# Проверим подключение:
print(page.status_code)

new_news = []
news = []

# Самое время воспользоваться BeautifulSoup4 и скормить ему наш page,
# указав в кавычках как он нам поможет 'html.parcer':
soup = BeautifulSoup(page.text, "html.parser")
# Если попросить его показать, что он там сохранил:
# print(soup)

# Теперь воспользуемся функцией поиска в BeautifulSoup4:
news = soup.findAll('a', class_='lenta')

for news_item in news:
    if news_item.find('span', class_='time2 time3') is not None:
        new_news.append(news_item.text)

print(f"{news_item =}")
