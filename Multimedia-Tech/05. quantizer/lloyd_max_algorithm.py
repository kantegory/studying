import numpy as np
from numpy import random
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error as mse
from copy import deepcopy


def create_data(mu, sigma, size):
    return random.normal(mu, sigma, size=size)


def quantize(data, centroids):
    for i in range(len(data)):
        for k in range(len(centroids) - 1):
            if (data[i] > centroids[k]) and (data[i] < centroids[k + 1]):
                data[i] = centroids[k]
    return data


def set_intervals(data, centroids, ax=1):
    return np.linalg.norm(data - centroids, axis=ax)


def paint_plot(data, restored_data, centroids):
    for i in range(len(centroids)):
        plt.plot([0, len(restored_data)], [centroids[i], centroids[i]], color='#000000')
    plt.plot(data, marker='o', ls='-', color='red')
    plt.plot(restored_data, marker='o', color='#4682B4')
    plt.show()


def predict(data, quants):

    size = len(data)
    data_uniq = np.unique(data)
    data_uniq_num = [i for i in range(len(np.unique(data)))]

    centroids = random.choice(data, quants, replace=False)
    clusters = np.zeros(size)

    for k in range(size):
        for j in range(quants):
            if data[k] == data_uniq[j]:
                data[k] = data_uniq_num[j]
        clusters[k] = data[k]

    while True:
        centroids_old = deepcopy(centroids)
        error = set_intervals(centroids, centroids_old, None)
        if error == 0:
            clusters = clusters.astype(int)
            centroids = centroids
            return centroids, clusters


def entropy(data, base=None):
    
    value, counts = np.unique(data, return_counts=True)
    norm_counts = counts / counts.sum()
    base = np.e if base is None else base

    return -(norm_counts * np.log(norm_counts)/np.log(base)).sum()


def main():
    mu = 0
    sigma = 1
    size = 100
    quants = 9
    data = create_data(mu, sigma, size)
    copydata = deepcopy(data)
    centroids, clusters = predict(data, quants)
    centroids = sorted(centroids)
    _min = min(data)
    restored_data = quantize(copydata, centroids)
    restored_data = np.clip(restored_data, min(centroids), max(centroids))
    paint_plot(copydata, restored_data, centroids)
    print('mse:', mse(copydata, restored_data))
    print('entropy of data:', entropy(copydata))
    print('entropy of restored data:', entropy(restored_data))


if __name__ == "__main__":
    main()
