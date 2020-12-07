import json
from collections import Counter

# Counter count the every occurrences of item

with open('static/articles.json', 'r') as f:
    articles = json.loads(f.read())


times = []
months = []
weeks = []
authors = []
categories = []

for article in articles:
    times.append(article['reading_time'])
    average_time = sum(times)/float(len(times))
    average_time = round(average_time, 2)

    months.append(article['month'])
    months_count = Counter(months)

    weeks.append(article['weekday'])
    weeks_count = Counter(weeks)

    authors.append(article['author'])
    authors_count = Counter(authors)

    categories += article['catigories']
    categories_count = Counter(categories)


print("the average time", average_time)
print('Post by months', months_count)
print('Post by Weeks', weeks_count)
print('Post by Author', authors_count)
print('Post bt category', categories_count)


states = {
    'reading_time': average_time,
    'num_articles': len(articles)
}

with open('static/states.json', 'w') as f:
    json.dump(states, f)

with open('static/weekday.json', 'w') as f:
    json.dump(weeks_count, f)

with open('static/month.json', 'w') as f:
    json.dump(months_count, f)

with open('static/category.json', 'w') as f:
    json.dump(categories_count, f)

with open('static/author.json', 'w') as f:
    json.dump(authors_count, f)






