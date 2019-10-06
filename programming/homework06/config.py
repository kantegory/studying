from bottle import (
    route, run, template, request, redirect
)
from parse import get_news, extract_next_page
from db import News, session
from scripts import save
from classify import Classifier

s = session()
classifier = Classifier()
mark_news = s.query(News).filter(News.label != None).all()
x_title = [row.title for row in mark_news]
y_lable = [row.label for row in mark_news]
classifier.fit(x_title, y_lable)
