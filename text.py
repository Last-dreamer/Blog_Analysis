import requests
from bs4 import BeautifulSoup
from dateutil import parser
from textstat.textstat import textstat

# textstat will allow us reading level of an article

# get around by that i am not a bot..
headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
    'referrer': 'https://google.com'
}


url = 'https://blog.frame.io/2018/10/01/womans-experience-cutting-blockbusterrs/'


def parse_page(url):
    r = requests.get(url, headers=headers)
    html = r.text.strip()
    soup = BeautifulSoup(html, 'lxml')

    #  header
    header_text = soup.find(class_='entry-header')
    read_time = extract_time(header_text)
    title = extract_title(header_text)

    author = extract_author(header_text)
    categories = extract_categories(header_text)

    date = extract_date(header_text)
    dt = parser.parse(date)
    month = dt.strftime("%B")
    weekday = dt.strftime("%A")
    year = dt.strftime("%Y")

    #  body content
    body_content = soup.find(class_='entry-content')
    word_count = len(body_content.text.split())
    reading_level = textstat.flesch_kincaid_grade(body_content.text)

    links = body_content.find_all('a')
    links_count = len(links)

    images = body_content.find_all('img')
    images_count = len(images)

    page_date = {
        'reading_time': read_time,
        'title': title,
        'author': author,
        'categories': categories,
        'date': date,
        'month': month,
        'weekday': weekday,
        'year': year,
        'total word': word_count,
        'reading level': reading_level,
        'total links': links_count,
        'total images': images_count

    }
    return page_date


def extract_time(header):
    html_str = header.find(class_='read-time')
    time_str = html_str.contents[0].strip().lower().split()[0]
    time_int = int(time_str)
    return time_int


def extract_title(header):
    html_str = header.find(class_='post-meta-title')
    title_str = html_str.contents[0].strip()
    return title_str


def extract_author(header):
    html_str = header.find(class_="author-name")
    author_name = html_str.find('a').contents[0].strip()
    return author_name


def extract_categories(header):
    html_str = header.find(class_="single-post-cat")
    categories = html_str.findAll('a')
    names = []
    for links in categories:
        name = links.contents[0].strip().lower()
        names.append(name)
    return names


def extract_date(header):
    html_str = header.find(class_="single-post-date")
    date = html_str.contents[0].strip()
    return date


exp = parse_page(url)

print(exp)
