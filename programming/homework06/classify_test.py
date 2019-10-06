import csv
import string
from classify import Classifier


def clean(s):
    translator = str.maketrans("", "", string.punctuation)
    return s.translate(translator)


with open('SMSSpamCollection.csv') as f:
    data = list(csv.reader(f, delimiter="\t"))
X, y = [], []
for target, msg in data:
    X.append(msg)
    y.append(target)
X = [clean(x).lower() for x in X]
X_train, y_train, X_test, y_test = X[0:3900], y[0:3900], X[3900:], y[3900:]

test_model = Classifier()
test_model.fit(X_train, y_train)
print(test_model.score(X_test, y_test))
