import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

from print_methods import print_data

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
        self.data_frame = pd.read_csv(filepath)

    def pre_process_data(self):
        pass

    def print_data(self):
        print_data(self.data_frame)

    def split_data(self, output_variable_name, test_size = 0.2):
        X = self.data_frame.drop(output_variable_name, axis = 1)
        # TODO: delete this, support cat variables
        X = X.select_dtypes(include = [np.number])

        y = self.data_frame[output_variable_name]
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(X, y, test_size = test_size)

    def normalize_data(self):
        # TODO: do this
        pass

    def get_X_train(self):
        return self.X_train

    def get_y_train(self):
        return self.y_train

    def get_X_test(self):
        return self.X_test

    def get_y_test(self):
        return self.y_test

    def get_number_of_columns(self):
        return self.get_X_train().columns
