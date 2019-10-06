import re
from db import News, session


def split_row(string):
    return list(filter(None, re.split('\W|\d', string)))


def save(pre_base):
    s = session()
    rows = s.query(News).filter(not News.label).all()
    labels = []
    for row in rows:
        labels.append(row.title)
    for cur_row in pre_base:
        if cur_row['title'] not in labels:
            news = News(title=cur_row['title'],
                        announce=cur_row['announce'],
                        url=cur_row['url'])
            s.add(news)
    s.commit()
