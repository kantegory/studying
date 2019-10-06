import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets


class LogisticRegression:
    def __init__(self, alpha=0.001, max_iter=5000):
        self.alpha = alpha
        self.max_iter = max_iter

    def fit(self, X_train, y_train):
        m = y_train.size
        X = X_train.copy()
        X = np.insert(X, 0, 1, axis=1)
        t = X.T
        theta = np.zeros(X.shape[1])

        for n in range(self.max_iter):
            z = np.dot(theta, t)
            sigma = 1 / (1 + np.exp(-z))
            theta -= self.alpha * (1 / m) * np.dot((sigma - y_train), X)

        self.intercept_ = theta[0]
        self.coef_ = theta[1:]

        return self.coef_, self.intercept_

    def predict(self, X_test):
        pred = []
        for i in range(len(X_test)):
            z = self.intercept_ + np.sum(X_test[i] * self.coef_)
            sigma = 1 / (1 + np.exp(-z))

            if sigma >= 0.5:
                pred.append(1)
            else:
                pred.append(0)

        return pred

    def predict_proba(self, X_test):
        return [(1 / (1 + np.exp(-(self.intercept_ + np.sum(X_test[i] * self.coef_)))), 1 - 1 / (1 + np.exp(-(self.intercept_ + np.sum(X_test[i] * self.coef_))))) for i in range(len(X_test))]


if __name__ == '__main__':
    df = datasets.load_iris()
    X = df.data[:100, :2]
    y = df.target[:100]
    model = LogisticRegression()
    model.fit(X, y)
    model.predict(X)
    model.predict_proba(X)
    setosa = plt.scatter(X[:50, 0], X[:50, 1], c='b')
    versicolor = plt.scatter(X[50:, 0], X[50:, 1], c='r')
    plt.xlabel("Sepal Length")
    plt.ylabel("Sepal Width")
    plt.legend((setosa, versicolor), ("Setosa", "Versicolor"))
    plt.show()
