from sklearn.feature_selection import RFE
from sklearn.decomposition import PCA

from sklearn.tree import DecisionTreeClassifier

from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline

from sklearn_pandas import DataFrameMapper
import pandas as pd

def recursive_feature_elimination(X, y, n):
    clf = DecisionTreeClassifier(random_state = 0)
    rfe = RFE(clf, n, step = 1)
    rfe.fit(X, y)
    ranking = rfe.ranking_

    from neural_network.neural_network import NeuralNetwork
    from math import ceil

    v = []
    c = 0
    for r in ranking:
        if r == 1:
            v.append(1)
            c += 1
        else:
            v.append(0)
    a = [ceil(c / 2)]
    ann = NeuralNetwork(v, a)
    ann.cross_val_train(X, y)

    header_text = "(Recursive Feature Elimination)"
    header_decorator = "="

    output = ""
    output += "Variables: \n"

    for i, r in enumerate(ranking):
        if r == 1:
            output += "    %s\n" % X.columns[i]
    
    output += ("Accuracy ANN:  %02f\n" % ann.get_accuracy())

    repeat_hd = len(max(output.split("\n"), key = len)) - len(header_text)
    repeat_hd = max(ceil(repeat_hd / 2), 3)

    header_text = header_decorator * repeat_hd + header_text + header_decorator * repeat_hd
    footer_text = header_decorator * len(header_text)
    print("")
    print(header_text, "\n")
    print(output)
    print(footer_text, "\n")

    return ranking

def principal_components_analysis(X, y, variance):
    X_copy = X.copy()
    pca = PCA(variance)
    principal_components = pca.fit_transform(X_copy)
    
    cols = []
    for i in range(pca.n_components_):
        cols.append("PC-%02d" % (i + 1))

    new_X = pd.DataFrame(data = principal_components, columns = cols)

    from neural_network.neural_network import NeuralNetwork
    from math import ceil

    v = [1] * len(new_X.columns)
    a = [ceil(len(v) / 2)]
    ann = NeuralNetwork(v, a)
    ann.cross_val_train(new_X, y)

    v_sum = 0
    for v in pca.explained_variance_ratio_:
        v_sum += v

    header_text = "(Principal Components Analysis)"
    header_decorator = "="

    output = ""
    output += ("Variance:       %02f\n" % v_sum)
    output += ("Components #:  %d\n" % pca.n_components_)
    output += ("Accuracy ANN:  %02f\n" % ann.get_accuracy())

    repeat_hd = len(max(output.split("\n"), key = len)) - len(header_text)
    repeat_hd = max(ceil(repeat_hd / 2), 3)

    header_text = header_decorator * repeat_hd + header_text + header_decorator * repeat_hd
    footer_text = header_decorator * len(header_text)
    print(header_text, "\n")
    print(output)
    print(footer_text, "\n")



def scale_data_frame(df, excluded_variables):
    scaled_features = df.copy()

    non_categorial_cols = scaled_features.columns.difference(excluded_variables)

    features = scaled_features[non_categorial_cols]
    
    scaler = StandardScaler().fit(features.values)
    features = scaler.transform(features.values)

    scaled_features[non_categorial_cols] = features
    


    return scaled_features
