import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


class GDRegressor:
    def __init__(self, alpha=0.0001, max_iter=2000):
        self.alpha = alpha
        self.max_iter = max_iter
        self.theta_all = [0] * self.max_iter
        self.cost = [0] * self.max_iter

    def fit(self, X_train, y_train):
        """
        Обучаем модель на данных
        :param X_train: матрица признаков
        :param y_train: матрица ответов
        :return: coef_ - вектор оценок для theta_i (i - значение от 1 до p, p - количество признаков),
        intercept_ - оценённое значение для theta_0
        """
        X = X_train.copy()
        X.insert(0, "Ones", np.ones(len(X)))
        t = X.T
        m = y_train.size
        theta = np.zeros(X.shape[1])
        
        for i in range(1, self.max_iter):
            theta -= self.alpha * (1 / m) * (np.dot(t, (np.dot(X, theta) - y_train)))
            self.theta_all[i] = theta
            self.cost[i] = np.sum((theta * X.as_matrix() - y_train.reshape((m, 1))) ** 2) / (2 * m)

        self.coef_ = theta[1]
        self.intercept_ = theta[0]

        return self.coef_, self.intercept_

    def predict(self, X_test):
        """
        Прогнозируем вектор для тестовой выборки
        :param X_test: тестовая выборка
        :return: вектор прогнозов для новых данных (произведение тестовой выборки на вектор весов)
        """
        
        return self.intercept_ + self.coef_ * X_test


def rmse(y_hat, y):
    """
    Считаем среднеквадратичную ошибку
    :param y_hat: изначальный вектор
    :param y: вектор прогнозов, сформированный в predict
    :return: среднеквадратичная ошибка
    """
    m = y.size
    error = 0
    for i in range(m):
        error = ((sum(y_hat.iloc[i] - y.iloc[i]) ** 2) / m) ** 0.5
    return error


def r_squared(y_hat, y):
    """
    Считаем коэффициент детерминации
    :param y_hat: изначальный вектор
    :param y: вектор прогнозов, сформированный в predict
    :return: коэффициент детерминации
    """
    m = y.size
    coef = 0
    for i in range(m):
        coef = 1 - (np.sum((y.iloc[i] - y_hat.iloc[i]) ** 2) / (np.sum((y.iloc[i] - y.mean()) ** 2)))
    return coef


if __name__ == '__main__':
    df = pd.read_csv('brain_size.csv')
    X = df.iloc[:, 1:2]
    y = df['VIQ']
    model = GDRegressor()
    model.fit(X, y)
    y_pred = model.predict(X)
    rmse(y_pred, y)
    r_squared(y_pred, y)
    df.plot(kind='scatter', x="FSIQ", y="VIQ")
    plt.plot(X, model.coef_ * X + model.intercept_, 'r')
    plt.show()
