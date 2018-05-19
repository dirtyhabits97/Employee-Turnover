import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

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
        print('\n===================REPORTE DE VARIABLES CUANTITATIVAS=================')
        print(self.data_frame.describe().transpose())
        print('\n===================REPORTE DE VARIABLES CUALITATIVAS=================')
        print(self.data_frame.describe(exclude = [np.number]).transpose())
        print('\n=======================ESTRUCTURA=======================')
        print(self.data_frame.shape)
        print('\n==========================TIPOS=========================')
        print(self.data_frame.dtypes)

    def split_data(self, output_variable_name, test_size = 0.2):
        input = self.data_frame.drop(output_variable_name, axis = 1)
        print("*********************************************************")
        print(len(input.columns))
        input = input.select_dtypes( include = [np.number])
        print(len(input.columns))
        print("*********************************************************")

        output = self.data_frame[output_variable_name]
        self.input_train, input_test, self.output_train, output_test = train_test_split(input, output, test_size = test_size)
        self.input_test, self.input_test_final, self.output_test, self.output_test_final = train_test_split(input_test, output_test, test_size = 0.5)

    def normalize_data(self):
        # TODO: do this
        pass

    def get_X_train(self):
        return self.input_train

    def get_y_train(self):
        return self.output_train

    def get_X_test(self):
        return self.input_test

    def get_y_test(self):
        return self.output_test

    def get_X_test_final(self):
        return self.input_test_final
    
    def get_y_test_final(self):
        return self.output_test_final

    def get_number_of_columns(self):
        return self.get_X_train().columns
