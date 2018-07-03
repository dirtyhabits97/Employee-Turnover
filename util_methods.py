from random import randint, uniform, sample
from data_manager import DataManager

from settings import MIN_NUMBER_OF_VARIABLES, MAX_NUMBER_OF_VARIABLES
from settings import MIN_NUMBER_OF_LAYERS, MAX_NUMBER_OF_LAYERS
from settings import MIN_NUMBER_OF_NODES, MAX_NUMBER_OF_NODES

def select_variables(size = DataManager.shared().get_number_of_columns()):
    number_of_variables = randint(MIN_NUMBER_OF_VARIABLES, MAX_NUMBER_OF_VARIABLES)
    variables_to_use = sample(range(0, len(size)), number_of_variables)
    return variables_to_use

def select_arquitecture():
    nodes = []
    number_of_layers = randint(MIN_NUMBER_OF_LAYERS, MAX_NUMBER_OF_LAYERS)
    for _ in range(0, number_of_layers):
        number_of_nodes = randint(MIN_NUMBER_OF_NODES, MAX_NUMBER_OF_NODES)
        nodes.append(number_of_nodes)
    return nodes

    
