import requests
from bs4 import BeautifulSoup
import text
import json


headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
    'referrer': 'https://google.com'
}

url = 'https://blog.frame.io/category/behind-the-scenes/'

articles_store = []


def parse_category(url):
    r = requests.get(url, headers=headers)
    html = r.text.strip()
    soup = BeautifulSoup(html, 'lxml')

    articles = soup.findAll(class_='post-content')

    for article in articles:
        title = article.find(class_='post-meta-title')
        link = title.contents[0]['href']
        print('Parsing URL :'+link+'\n')
        # the whole page
        page = text.parse_page(link)
        articles_store.append(page)

    next_link = findNextLink(soup)

    if next_link is not None:
        print('next link', next_link)
        parse_category(next_link)

    return None


def findNextLink(soup_item):
    bottom_nav = soup_item.find(class_='navigation')

    if bottom_nav == None:
        return None

    links = bottom_nav.findAll('a')
    next_page = links[-1]

    if next_page.contents[0] == 'Next':
        next_link = next_page['href']
        return next_link

    return None


categories = ['post-production',
              'color-correction', 'business',
              'workflow', 'behind-the-scenes',
              'production', 'announcement']


#  extraction all categories ...

for category in categories:
    url = 'https://blog.frame.io/category/' + category + '/'
    parse_category(url)


print(len(articles_store))

print(articles_store[0])

with open('static/articles.json', 'w') as f:
    json.dump(articles_store, f)

