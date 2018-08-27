from sklearn.feature_selection import RFE
from sklearn.decomposition import PCA

from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVR

def recursive_feature_elimination(X, y, n):
    clf = DecisionTreeClassifier(random_state = 0)
    # clf = SVR(kernel = "linear")
    rfe = RFE(clf, n, step = 1)
    rfe.fit(X, y)
    return rfe.ranking_

def principal_components_analysis(X):
    pca = PCA(n_components = 5)
    pca.fit(X)
    print(pca.n_components_)
