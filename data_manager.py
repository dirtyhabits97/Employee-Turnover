import pandas as pd

class DataManager:
    __instance == None

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
