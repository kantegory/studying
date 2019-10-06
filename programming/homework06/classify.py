import math
from scripts import split_row


class Classifier:

    def __init__(self, alpha=1):
        self.alpha = alpha

    def fit(self, x, y):
        """ Fit Naive Bayes classifier according to X, y. """
        self.labels = [i for i in set(y)]
        self.labels.sort()
        classes = len(self.labels)
        number_of_labels = [0] * classes
        for i in range(len(y)):
            """ count a number of every label """
            y[i] = self.labels.index(y[i]) + 1
            number_of_labels[y[i] - 1] += 1
        self.attrs = [[] for _ in range(classes * 2 + 1)]
        self.favorite_labels = [math.log(number / sum(number_of_labels)) for number in number_of_labels]
        for i in range(len(x)):
            words = split_row(x[i])
            for word in words:
                if word in self.attrs[0]:
                    self.attrs[y[i]][self.attrs[0].index(word)] += 1
                else:
                    self.attrs[0].append(word)
                    self.attrs[y[i]].append(1)
                    num_of_label = y[i]
                    for j in range(classes - 1):
                        num_of_label = (num_of_label % classes) + 1
                        self.attrs[num_of_label].append(0)
                    for col in range(classes + 1, classes * 2 + 1):
                        self.attrs[col].append(0)
        words_on_labels = [sum(self.attrs[i + 1]) for i in range(classes)]

        for row in range(len(self.attrs[0])):
            for col in range(classes + 1, classes * 2 + 1):
                self.attrs[col][row] = (self.attrs[col - classes][row] + self.alpha) / \
                                       (words_on_labels[col - classes - 1] + self.alpha *
                                        len(self.attrs[0]))

    def predict(self, x):
        """ Perform classification on an array of test vectors X. """
        labels = []
        classes = len(self.labels)
        for string in x:
            prob_labels = [i for i in self.favorite_labels]
            words = split_row(string)
            for word in words:
                if word in self.attrs[0]:
                    for i in range(classes):
                        prob_labels[i] += math.log(self.attrs[i + classes + 1][self.attrs[0].index(word)])
            for i in range(classes):
                if prob_labels[i] == max(prob_labels):
                    labels.append(self.labels[i])
                    break
        return labels

    def score(self, x_test, y_test):
        """ Returns the mean accuracy on the given test data and labels. """
        prediction = self.predict(x_test)
        count = 0
        for i in range(len(prediction)):
            if prediction[i] == y_test[i]:
                count += 1
        return count / len(y_test)
