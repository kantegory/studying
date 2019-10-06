from numpy import random
import numpy as np
from copy import deepcopy
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error as mse


def create_data(mu, sigma, size):
    return random.normal(mu, sigma, size=size)


def count_step(data, quants):
    return (max(data) - min(data)) / max(1, quants - 1)


def quantize(data, step):
    return np.round([(i - min(data)) / step for i in data])


def restore(data, step, _min):
    return [i * step + _min for i in data]


def set_intervals(step, quants, _min):
    return [step * i + _min for i in range(quants)]


def paint_plot(data, restored_data, intervals):
    for i in range(len(intervals)):
        plt.plot([0, len(restored_data)], [intervals[i], intervals[i]], color='#000000')
    plt.plot(data, marker='o', ls='-', color='red')
    plt.plot(restored_data, marker='o', color='#4682B4')
    plt.show()


def main():
    mu = 5  # expected value
    sigma = 1  # dispersion
    size = 100
    quants = 8
    data = create_data(mu, sigma, size)
    step = count_step(data, quants)
    _min = min(data)
    quanted_data = quantize(data, step)
    restored_data = restore(quanted_data, step, _min)
    intervals = set_intervals(step, quants, _min)
    restored_data = np.clip(restored_data, min(intervals), max(intervals))
    paint_plot(data, restored_data, intervals)
    print('mse:', mse(data, restored_data))
    print('entropy of data:', entropy(data))
    print('entropy of restored data:', entropy(restored_data))


if __name__ == '__main__':
    main()
