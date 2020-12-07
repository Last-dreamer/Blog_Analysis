import os
import operator

from flask import Flask, render_template, json, url_for

app = Flask(__name__)


@app.route('/')
def index():
    SITE_ROOT = os.path.realpath(os.path.dirname(__file__))

    states_url = os.path.join(SITE_ROOT, 'static', 'states.json')
    states = json.load(open(states_url))

    category_url = os.path.join(SITE_ROOT, 'static', 'category.json')
    category = json.load(open(category_url))
    sorted_category = sorted(category.items(), key=operator.itemgetter(1), reverse=True)

    author_url = os.path.join(SITE_ROOT, 'static', 'author.json')
    author = json.load(open(author_url))
    sorted_author = sorted(author.items(), key=operator.itemgetter(1), reverse=True)

    weekday_url = os.path.join(SITE_ROOT, 'static',  'weekday.json')
    weekday = json.load(open(weekday_url))

    return render_template('blog.html', states=states, category=sorted_category, author=sorted_author, weekday=weekday)


if __name__ == '__main__':
    app.run(debug=True)



