from bottle import (
    route, run, template, request, redirect
)

from scraputils import get_news
from db import News, session, create_db
from bayes import NaiveBayesClassifier


@route("/all")
def all_news():
    s = session()
    rows = s.query(News).all()
    return template('news_template2', rows=rows)

@route("/news")
def news_list():
    s = session()
    rows = s.query(News).filter(News.label == None).all()
    return template('news_template', rows=rows)


@route("/add_label/", method='GET')
def add_label():
    s = session()
    label = request.GET.get('label', '')
    id = int(request.GET.get('id', ''))
    row = s.query(News).filter(News.id == id).one()
    row.label = label
    s.add(row)
    s.commit()
    redirect("/all")


@route("/update")
def update_news():
    url = "https://news.ycombinator.com/"
    lst = get_news(url)
    create_db(lst)
    redirect("/news")


@route("/classify")
def classify_news():
    # PUT YOUR CODE HERE
    pass


if __name__ == "__main__":
    run(host="localhost", port=8080)

