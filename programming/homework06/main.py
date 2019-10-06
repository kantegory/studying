from config import *


@route('/')
@route('/news')
def news_list():
    rows = s.query(News).filter(News.label == None).all()
    return template('news_template', rows=rows)


@route("/add_label/")
def add_label():
    label = request.query.label
    row_id = request.query.id
    row = s.query(News).filter(News.id == row_id).one()
    row.label = label
    s.commit()
    if request.query.classify == 'True':
        redirect('/classify')
    else:
        redirect('/news')


@route('/update')
def update_news():
    save(get_news(extract_next_page('https://tproger.ru/amp/')))
    redirect('/')


@route('/classify')
def classify_news():
    recently_mark_news = s.query(News).filter(News.title not in x_title and News.label != None).all()
    title_extra = [row.title for row in recently_mark_news]
    label_extra = [row.label for row in recently_mark_news]
    classifier.fit(title_extra, label_extra)
    not_mark_news = s.query(News).filter(News.label == None).all()
    x = [row.title for row in not_mark_news]
    labels = classifier.predict(x)
    for i in range(len(not_mark_news)):
        not_mark_news[i].label = labels[i]
    s.commit()
    classified_news = s.query(News).filter(News.label == 'good').all()
    return template('classify_template', rows=classified_news)


if __name__ == "__main__":
    run(host="localhost", port=8080)
