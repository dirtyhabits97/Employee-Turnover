from sklearn.feature_selection import RFE
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVR

def recursive_feature_elimination(X, y, n):
    clf = DecisionTreeClassifier(random_state = 0)
    # clf = SVR(kernel = "linear")
    rfe = RFE(clf, n, step = 1)
    rfe.fit(X, y)
    return rfe.ranking_
