from sklearn.feature_selection import RFE
from sklearn.decomposition import PCA

from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVR

from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline

from sklearn_pandas import DataFrameMapper
import pandas as pd

def recursive_feature_elimination(X, y, n):
    clf = DecisionTreeClassifier(random_state = 0)
    # clf = SVR(kernel = "linear")
    rfe = RFE(clf, n, step = 1)
    rfe.fit(X, y)
    return rfe.ranking_

def principal_components_analysis(df, variance):
    pca = PCA(variance)
    pca.fit(df)
    sum = 0
    for v in pca.explained_variance_ratio_:
        sum += v

    print("Total variance: ", sum)
    print("Components: ", pca.n_components_)
    # mapper = DataFrameMapper([(X.columns, StandardScaler())])
    # copy_X = X.copy()
    # scaled_features = mapper.fit_transform(copy_X, 4)
    # scaled_features_df = pd.DataFrame(scaled_features, index = X.index, columns = X.columns)
    # print(scaled_features_df.head(3))
    
    # pca = PCA()
    # pca.fit(scaled_features_df)
    # print(pca.explained_variance_ratio_)

def scale_data_frame(df, categorical_cols):
    scaled_features = df.copy()
    non_categorial_cols = scaled_features.columns.difference(categorical_cols)

    features = scaled_features[non_categorial_cols]
    
    scaler = StandardScaler().fit(features.values)
    features = scaler.transform(features.values)

    scaled_features[non_categorial_cols] = features
    return scaled_features
