from random import randint, uniform

MAX_NUMBER_OF_VARIABLES = 10
MIN_NUMBER_OF_VARIABLES = 5
MAX_NUMBER_OF_LAYERS = 4
MIN_NUMBER_OF_LAYERS = 1
MAX_NUMBER_OF_NODES = 10
MIN_NUMBER_OF_NODES = 3
MAX_LEARNING_RATE = 0.10
MIN_LEARNING_RATE = 0.01

def select_variables(size):
    variables = set()
    number_of_variables = randint(MIN_NUMBER_OF_VARIABLES, MAX_NUMBER_OF_VARIABLES)
    while len(variables) != number_of_variables:
        variable = randint(0,size - 1)
        if variable not in variables:
            variables.add(variable)
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
    