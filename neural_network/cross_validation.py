from sklearn.model_selection import KFold, cross_val_score, cross_val_predict
from sklearn.metrics import accuracy_score

import numpy as np
class CrossValidation:

    @staticmethod
    def cross_validate(clf, X, y):
        kf = KFold(n_splits = 10, shuffle = True)
        scores = []

        for train_index, test_index in kf.split(X):
            clf.fit(X.iloc[train_index], y.iloc[train_index])
            # TODO: revisar este metodo
            score = clf.score(X.iloc[test_index], y.iloc[test_index])
            scores.append(score)
        
        s = np.array(scores)
        mean = s.mean()
        sd   = s.std()
        return mean, sd

    @staticmethod
    def cross_validation_score(clf, X, y):
        scores = cross_val_score(clf, X, y)
        mean   = scores.mean()
        sd     = scores.std()
        return mean, sd

    @staticmethod
    def cross_validation_predict(clf, X, y):
        y_pred = cross_val_predict(clf, X, y)
        return accuracy_score(y, y_pred)
