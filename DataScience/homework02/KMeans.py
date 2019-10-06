import pandas as pd
import numpy as np
from copy import deepcopy


def distance(v1, v2, ax=1):
    return np.linalg.norm(v1 - v2, axis=ax)


class KMeans:
    def __init__(self, n_clusters, max_iter=300):
        self.n_clusters = n_clusters
        self.max_iter = max_iter

    def fit(self, X):
        """
        Обучаем модель на тренировочной выборке
        :param X: вектор значений
        """
        
        n_samples = len(X)
        centroids = X[np.random.choice(X.shape[0], self.n_clusters, replace=False)]
        centroids_old = np.zeros(centroids.shape)
        clusters = np.zeros(n_samples)

        while True:
            for i in range(n_samples):
                distances = distance(X[i,], centroids)
                clusters[i] = distances.argmin()
                centroids_old = deepcopy(centroids)
            for k in range(self.n_clusters):
                centroids[k] = X[clusters == k,].mean(axis=0)
            error = distance(centroids, centroids_old, None)
            if error == 0:
                self.clusters = clusters.astype('int')
                self.centroids = centroids

    def predict(self, y):
        """
        Считаем центроиды по принадлежности к кластеру
        :param y: принадлежность элемента к кластеру
        :return: центроиды, принадлежность
        """
        
        y_uniq = np.unique(y)
        y_uniq_num = [i for i in range(len(np.unique(y)))]
        n_samples = len(X)
        clusters = np.zeros(n_samples)

        for k in range(n_samples):
            for j in range(self.n_clusters):
                if y[k][0] == y_uniq[j]:
                    y[k] = y_uniq_num[j]
            clusters[k] = y[k]

        centroids = X[np.random.choice(X.shape[0], self.n_clusters,
                                       replace=False)]
        
        while True:
            centroids_old = deepcopy(centroids)
            error = distance(centroids, centroids_old, None)
            if error == 0:
                self.clusters = clusters.astype(int)
                self.centroids = centroids
                return self.centroids, self.clusters


if __name__ == '__main__':
    data = pd.read_csv('iris.csv')
    model = KMeans(3)
    X = (data.loc[:, data.columns != 'Name']).as_matrix()
    y = (data.loc[:, data.columns == 'Name']).as_matrix()
    model.fit(X)
    print(model.predict(y))
