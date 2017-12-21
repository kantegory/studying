import requests
import time
from datetime import datetime
import plotly
import plotly.plotly as py
import plotly.graph_objs as go
import config
import numpy as np
import igraph
from igraph import plot, Graph
from collections import Counter

plotly.tools.set_credentials_file(username=config.plotlyUsername, api_key=config.plotlyApiKey)


def get(url, params={}, timeout=5, max_retries=5, backoff_factor=0.3):
    """ Выполнить GET-запрос
    :param url: адрес, на который необходимо выполнить запрос
    :param params: параметры запроса
    :param timeout: максимальное время ожидания ответа от сервера
    :param max_retries: максимальное число повторных запросов
    :param backoff_factor: коэффициент экспоненциального нарастания задержки
    """
    for attempt in range(max_retries):
        try:
            response = requests.get(url, params=params, timeout=timeout)
            return response
        except requests.exceptions.RequestException:
            if attempt == max_retries - 1:
                raise
            backoff_value = backoff_factor * (2 ** attempt)
            time.sleep(backoff_value)


def get_friends(user_id, fields=''):
    """ Вернуть данных о друзьях пользователя
    :param user_id: идентификатор пользователя, список друзей которого нужно получить
    :param fields: список полей, которые нужно получить для каждого пользователя
    """
    assert isinstance(user_id, int), "user_id must be positive integer"
    assert isinstance(fields, str), "fields must be string"
    assert user_id > 0, "user_id must be positive integer"
    query_params = {
        'domain': config.domain,
        'access_token': config.vkApiKey,
        'user_id': user_id,
        'fields': fields,
        'v': config.v
    }
    url = "{}/friends.get".format(config.domain)
    response = get(url, params=query_params)
    return response.json()


def age_predict(user_id):
    """ Наивный прогноз возраста по возрасту друзей
    Возраст считается как медиана среди возраста всех друзей пользователя
    :param user_id: идентификатор пользователя
    """
    assert isinstance(user_id, int), "user_id must be positive integer"
    assert user_id > 0, "user_id must be positive integer"
    getFriendsValue = get_friends(user_id, 'bdate')
    birthdays = [date.get('bdate') for date in getFriendsValue.get('response').get('items')]
    age = [2017 - int(birthdays[date][-4:]) for date in range(len(birthdays))
           if (birthdays[date]) and (len(birthdays[date]) >= 8)]
    return sum(age) // len(age)


def messages_get_history(user_id, offset=0, count=20):
    """ Получить историю переписки с указанным пользователем
    :param user_id: идентификатор пользователя, с которым нужно получить историю переписки
    :param offset: смещение в истории переписки
    :param count: число сообщений, которое нужно получить
    """
    assert isinstance(user_id, int), "user_id must be positive integer"
    assert user_id > 0, "user_id must be positive integer"
    assert isinstance(offset, int), "offset must be positive integer"
    assert offset >= 0, "user_id must be positive integer"
    assert count >= 0, "user_id must be positive integer"
    max_count = 200
    messages = []
    query_params = {
        'domain': config.domain,
        'access_token': config.vkApiKey,
        'user_id': user_id,
        'offset': offset,
        'count': min(count, max_count),
        'v': config.v
    }
    while count > 0:
        url = "{}/messages.getHistory".format(config.domain)
        response = get(url, params=query_params)
        count -= min(count, max_count)
        query_params['offset'] += 200
        query_params['count'] = min(count, max_count)
        messages += response.json()['response']['items']
        time.sleep(0.333333334)

    return messages


def count_dates_from_messages(messages):
    """ Получить список дат и их частот
    :param messages: список сообщений
    """
    date = [datetime.fromtimestamp(messages[i]['date']).strftime("%Y-%m-%d")
            for i in range(len(messages))]
    frequency = Counter(date)
    x = [date for date in frequency]
    y = [frequency[date] for date in frequency]
    return x, y


def plotly_messages_freq(freq_list):
    """ Построение графика с помощью Plot.ly
    :param freq_list: список дат и их частот
    """
    data = [go.Scatter(x=freq_list[0], y=freq_list[1])]
    py.plot(data)


def get_network(user_id, as_edgelist=True):
    users_ids = get_friends(user_id)['response']['items']
    edges = []
    matrix = np.zeros((len(users_ids), len(users_ids)))
    for i in range(len(users_ids)):
        time.sleep(0.33333334)
        response = get_friends(users_ids[i])
        if response.get('error'):
            continue
        friends = response['response']['items']
        for j in range(i + 1, len(users_ids)):
            if users_ids[j] in friends:
                if as_edgelist:
                    edges.append((i, j))
                else:
                    matrix[i][j] = 1
    if as_edgelist:
        return edges
    else:
        return matrix


def plot_graph(user_id):
    surnames = get_friends(user_id, 'last_name')
    vertices = [surnames['response']['items'][i]['last_name'] for i in range(len(surnames['response']['items']))]
    edges = get_network(user_id)
    g = Graph(vertex_attrs={"shape": "circle",
                            "label": vertices,
                            "size": 10},
              edges=edges, directed=False)

    N = len(vertices)
    visual_style = {
        "vertex_size": 20,
        "bbox": (2000, 2000),
        "margin": 100,
        "vertex_label_dist": 1.6,
        "edge_color": "gray",
        "autocurve": True,
        "layout": g.layout_fruchterman_reingold(
            maxiter=100000,
            area=N ** 2,
            repulserad=N ** 2)
    }

    clusters = g.community_multilevel()
    pal = igraph.drawing.colors.ClusterColoringPalette(len(clusters))
    g.vs['color'] = pal.get_many(clusters.membership)

    plot(g, **visual_style)
