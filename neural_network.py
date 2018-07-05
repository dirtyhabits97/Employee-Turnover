from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score
from util_methods import select_arquitecture, select_variables
from genetic_algorithm import Chromosome
from random import randint, random
from cross_validation import CrossValidation
from settings import MIN_NUMBER_OF_NODES, MAX_NUMBER_OF_NODES

class NeuralNetwork(MLPClassifier, Chromosome):

    # ******************************************************************************
    # Neural Network methods
    # ******************************************************************************
    
    def __init__(self, arquitecture = None, variables = None):
        self.selected_arquitecture = arquitecture if arquitecture is not None else select_arquitecture()
        self.selected_variables = variables if variables is not None else select_variables()

        self.predictions = []
        self.accuracy = 0
        self.standardDeviation = 0

        # MLP Classifier init
        # http://scikit-learn.org/stable/modules/generated/sklearn.neural_network.MLPClassifier.html
        MLPClassifier.__init__(
            self,
            hidden_layer_sizes = tuple(self.selected_arquitecture),
            learning_rate = 'constant',
            learning_rate_init = 0.001,
            max_iter = 3000
        )

    def filter_variables(self, X):
        variables_to_drop = []
        for i in range(0, len(self.selected_variables)):
            if self.selected_variables[i] != 1:
                variables_to_drop.append(i)

        new_X = X.drop(X.columns[variables_to_drop], axis = 1)
        return new_X

    def cross_val_train(self, X, y):
        mean, sd = CrossValidation.cross_validate(self, X, y)

        self.accuracy = mean
        self.standardDeviation = sd
    
    # ******************************************************************************
    # Chromosome methods
    # ******************************************************************************

    def get_fitness(self):
        return self.accuracy

    def get_genes(self):
        # TODO: implement selected variables
        genes = (self.selected_variables, self.selected_arquitecture)
        return genes

    def calculate_fitness(self, X, y):
        if self.accuracy != 0: return
        new_X = self.filter_variables(X)
        self.cross_val_train(new_X, y)

    # Crossover methods
    def crossover_children(self, chromosome):
        variables = chromosome.get_genes()[0]
        arquitecture = chromosome.get_genes()[1]
        v1, v2 = self.cross_variables(variables)
        a1, a2 = self.cross_arquitecture(arquitecture)

        children_one = NeuralNetwork.instantiate_with_attributes(v1, a1)
        children_two = NeuralNetwork.instantiate_with_attributes(v2, a2)
        return children_one, children_two

    def cross_variables(self, variables):
        variables_one, variables_two = _crossover_array(
            self.selected_variables, 
            variables
        )
        return variables_one, variables_two

    def cross_arquitecture(self, arquitecture):
        arquitecture_one, arquitecture_two = _crossover_array(
            self.selected_arquitecture,
            arquitecture
        )
        return arquitecture_one, arquitecture_two

    def mutate(self, chromosome, mutation_rate):

        variables = chromosome.get_genes()[0]
        arquitecture = chromosome.get_genes()[1]

        for i in range(0 , len(variables)):
            if random() < mutation_rate:
                variables[i] = 0 if variables[i] == 1 else 1
            
        for i in range(0, len(arquitecture)):
            if random() < mutation_rate:
                new_v = arquitecture[i]
                while new_v == arquitecture[i]:
                    new_v = randint(MIN_NUMBER_OF_NODES, MAX_NUMBER_OF_NODES)
                arquitecture[i] = new_v

        self.selected_variables = variables
        self.selected_arquitecture = arquitecture

    def __str__(self):
        return self.get_genes().__str__()

    def __len__(self):
        return len(self.__str__())

    # ******************************************************************************
    # Static methods
    # ******************************************************************************

    @staticmethod
    # instantiate with random parameters
    # used to create the first generation of neural network population
    def instantiate():
        return NeuralNetwork()


    @staticmethod
    def instantiate_with_attributes(variables, arquitecture):
        ann = NeuralNetwork(
            variables = variables,
            arquitecture = arquitecture
        )
        return ann


def _crossover_array(arr1, arr2):
    l1 = arr1
    l2 = arr2

    crossover_idx = randint(0, min(len(l1), len(l2)))
    # first children
    children_one = l1[0:crossover_idx+1] + l2[crossover_idx+1:]
    # second children
    children_two = l2[0:crossover_idx+1] + l1[crossover_idx+1:]
    return children_one, children_two
