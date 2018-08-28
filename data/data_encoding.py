import pandas as pd
import numpy as np

from sklearn.feature_extraction import DictVectorizer

def one_hot_encode(df, cols):
    vec = DictVectorizer(dtype= np.int)

    records = df[cols].to_dict(orient = "records")
    
    vec_data = pd.DataFrame(vec.fit_transform(records).toarray())
    vec_data.columns = vec.get_feature_names()
    vec_data.index = df.index

    df = df.drop(cols, axis = 1)
    df = df.join(vec_data)
    return df

def binary_encode(df, cols):
    for col in cols:
        if col in df.columns:
            df[col] = df[col].astype('category')
            df[col] = df[col].cat.codes
    return df
