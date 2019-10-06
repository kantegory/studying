import requests
from bs4 import BeautifulSoup
links = [] # array for all of parsed urls

def get_page(url):
    try:
        response = requests.get(url)
        if response.ok:
            return response.text
        else:
            print("Error " + str(response.status_code))
            return False
    except requests.exceptions.ConnectTimeout:
        print('Oops. Connection timeout occured!')
    except requests.exceptions.ReadTimeout:
        print('Oops. Read timeout occured')
    except requests.exceptions.ConnectionError:
        print('Seems like dns lookup failed..')


def extract_news(page):
    """ Extract news from a given web page """
    articles = [page.findAll('div', {'class': 'amp-wp-content amp-wp-article-header amp-loop-list'})[j] for j in
                range(len(page.findAll('div', {'class': 'amp-wp-content amp-wp-article-header amp-loop-list'})))]
    return [{'url': articles[i].a['href'], 'title': articles[i].a.text, 'announce': articles[i].p.text}
            for i in range(len(articles))]


def extract_next_page(page):
    """ Extract next page URL """
    if url in links:
        response = get_page(links[-1])
        page = BeautifulSoup(response, 'html5lib')
        return page.find('div', {'class': 'next'}).a['href']
    else:
        links.append(url)
        return url


def get_news(url, n_pages=1):
    """ Collect news from a given web page """
    news = []
    while n_pages:
        print("Collecting data from page: {}".format(url))
        response = get_page(url)
        url = extract_next_page(url)
        page = BeautifulSoup(response, 'html5lib')
        news_list = extract_news(page)
        next_page = extract_next_page(page)
        news.extend(news_list)
        n_pages -= 1
    return news
