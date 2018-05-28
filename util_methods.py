from random import randint, uniform
from data_manager import DataManager

from settings import MIN_NUMBER_OF_VARIABLES, MAX_NUMBER_OF_VARIABLES
from settings import MIN_NUMBER_OF_LAYERS, MAX_NUMBER_OF_LAYERS
from settings import MIN_NUMBER_OF_NODES, MAX_NUMBER_OF_NODES
from settings import MIN_LEARNING_RATE, MAX_LEARNING_RATE

def select_variables(size = DataManager.shared().get_number_of_columns()):
    variables = []
    number_of_variables = randint(MIN_NUMBER_OF_VARIABLES, MAX_NUMBER_OF_VARIABLES)
    while len(variables) != number_of_variables:
        variable = randint(0,len(size) - 1)
        if variable not in variables:
            variables.append(variable)
    return variables

def select_arquitecture():
    nodes = []
    number_of_layers = randint(MIN_NUMBER_OF_LAYERS, MAX_NUMBER_OF_LAYERS)
    for _ in range(0, number_of_layers):
        number_of_nodes = randint(MIN_NUMBER_OF_NODES, MAX_NUMBER_OF_NODES)
        nodes.append(number_of_nodes)
    return nodes

def select_learning_rate():
    learning_rate = uniform(MIN_LEARNING_RATE, MAX_LEARNING_RATE)
    return round(learning_rate, 4)
    
