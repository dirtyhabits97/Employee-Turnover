from sklearn.neural_network import MLPClassifier

from helper_methods.util_methods import select_variables, select_arquitecture

from genetic_algorithm.chromosome import Chromosome
from .neural_network_components import Variable, Arquitecture

class NeuralNetwork(MLPClassifier, Chromosome):

    # ******************************************************************************
    # Neural Network methods
    # ******************************************************************************

    def __init__(self, variables = None, arquitecture = None):
        v = variables if variables else select_variables()
        # a = arquitecture if arquitecture else select_arquitecture()
        from math import ceil
        

        # E7 (f > 2)
        # [0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0, 1, 0, 1, 1, 0, 0, 1, 0, 0, 0]
        # v = [0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0, 1, 0, 1, 1, 0, 0, 1, 0, 0, 0]
        self.variables = Variable(v)
        a = [ceil(len(self.variables.used_variables()) / 2)]
        self.arquitecture = Arquitecture(a)

        self.accuracy = 0

        self.fitness = 0 # fitness = accuracy
        self.genes = (self.variables.raw(), self.arquitecture.raw())

        # MLP Classifier init
        # http://scikit-learn.org/stable/modules/generated/sklearn.neural_network.MLPClassifier.html
        MLPClassifier.__init__(
            self,
            hidden_layer_sizes = tuple(self.arquitecture.raw()),
            learning_rate = 'constant',
            learning_rate_init = 0.001,
            max_iter = 3000
        )

    def filter_variables(self, X):
        variables_to_drop = self.variables.unused_variables()

        # Delete the unused variables from the DataFrame
        new_X = X.drop(X.columns[variables_to_drop], axis = 1)
        return new_X

    def cross_val_train(self, X, y):
        from .cross_validation import CrossValidation
        mean_accuracy, _ = CrossValidation.cross_validate(self, X, y)
        self.accuracy = mean_accuracy
        self.fitness = self.accuracy

    def get_accuracy(self):
        return self.accuracy if self.accuracy else 0

    # ******************************************************************************
    # Chromosome methods
    # ******************************************************************************

    def calculate_fitness(self, X, y):
        if self.fitness != 0: return
        # Filter the unused variables
        new_X = self.filter_variables(X)
        # Apply cross validation training
        self.cross_val_train(new_X, y)

    def crossover_with(self, chromosome):
        v = chromosome.variables
        a = chromosome.arquitecture

        v1, v2 = self.variables.crossover_with(v)
        a1, a2 = self.arquitecture.crossover_with(a)

        # Instantiate the children chromosomes
        # based on the parent's chromosomes
        c1 = NeuralNetwork(v1, a1)
        c2 = NeuralNetwork(v2, a2)

        return c1, c2

    def mutate(self, mutation_rate):
        self.variables.mutate(mutation_rate)
        self.arquitecture.mutate(mutation_rate)

    # ******************************************************************************
    # Helper methods
    # ******************************************************************************

    def __str__(self):
        return self.get_genes().__str__()

    def __len__(self):
        return len(self.__str__())

    # ******************************************************************************
    # Static methods
    # ******************************************************************************
    
    @staticmethod
    def instantiate():
        return NeuralNetwork()