from random import randint, uniform, sample
from data_manager import DataManager

from settings import MIN_NUMBER_OF_VARIABLES, MAX_NUMBER_OF_VARIABLES
from settings import MIN_NUMBER_OF_LAYERS, MAX_NUMBER_OF_LAYERS
from settings import MIN_NUMBER_OF_NODES, MAX_NUMBER_OF_NODES

def select_variables(size = DataManager.shared().get_number_of_columns()):
    number_of_variables = randint(MIN_NUMBER_OF_VARIABLES, MAX_NUMBER_OF_VARIABLES)
    variables_to_use = sample(range(0, len(size)), number_of_variables)
    variables = []
    for i in range(0, len(size)):
        if i in variables_to_use:
            variables.append(1)
        else:
            variables.append(0)
    return variables

def select_arquitecture():
    nodes = []
    number_of_layers = randint(MIN_NUMBER_OF_LAYERS, MAX_NUMBER_OF_LAYERS)
    for _ in range(0, number_of_layers):
        number_of_nodes = randint(MIN_NUMBER_OF_NODES, MAX_NUMBER_OF_NODES)
        nodes.append(number_of_nodes)
    return nodes

    
def crossover_array(arr1, arr2):
    l1 = arr1
    l2 = arr2

    crossover_idx = randint(0, min(len(l1), len(l2)))
    # first children
    children_one = l1[0:crossover_idx+1] + l2[crossover_idx+1:]
    # second children
    children_two = l2[0:crossover_idx+1] + l1[crossover_idx+1:]
    return children_one, children_two