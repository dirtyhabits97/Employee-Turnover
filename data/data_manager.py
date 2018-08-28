import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

from helper_methods.print_methods import print_data, print_variables
from .data_encoding import one_hot_encode, binary_encode
from .feature_selection import recursive_feature_elimination, principal_components_analysis, scale_data_frame

class DataManager:
    __instance = None

    @staticmethod
    def shared():
        if DataManager.__instance == None:
            DataManager()
        return DataManager.__instance

    def __init__(self):
        if DataManager.__instance != None:
            raise Exception("already instantiated")
        else:
            DataManager.__instance = self
    
    def read_data(self, filepath):
        self.data_frame_original = pd.read_csv(filepath)
        self.data_frame = self.data_frame_original.copy()

    def scale_data(self, excluded_variables):
        self.data_frame = scale_data_frame(self.data_frame, excluded_variables)

    def drop_columns(self, cols):
        self.data_frame = self.data_frame.drop(cols, axis = 1)
    
    def one_hot_encode_data(self, variables):
        self.data_frame = one_hot_encode(self.data_frame, variables)

    def binary_encode_data(self, variables):
        self.data_frame = binary_encode(self.data_frame, variables)

    def split_data(self, output_variable_name, test_size = 0.2):
        self.X = self.data_frame.drop(output_variable_name, axis = 1)
        self.y = self.data_frame[output_variable_name]
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(self.X, self.y, test_size = test_size)

    def get_X_train(self):
        return self.X_train

    def get_y_train(self):
        return self.y_train

    def get_X_test(self):
        return self.X_test

    def get_y_test(self):
        return self.y_test

    def get_number_of_columns(self):
        return len(self.get_X_train().columns)

# ******************************************************************************
# Data Analysis Methods
# ******************************************************************************

    def rfe_analysis(self, number_of_relevant_v):
        recursive_feature_elimination(self.X_train, self.y_train, number_of_relevant_v)

    def pca_analysis(self, variance):
        principal_components_analysis(self.X_train, self.y_train, variance)

# ******************************************************************************
# Print Data Methods
# ******************************************************************************

    def print_data(self):
        print_data(self.data_frame)

    def print_variables(self):
        print_variables(self.get_X_train())
