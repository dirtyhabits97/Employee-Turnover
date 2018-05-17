from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score
from util_methods import select_arquitecture, select_learning_rate, select_variables
from genetic_algorithm import Chromosome
from random import randint

LEARNING_RATE_PROBABILITY = 25

class NeuralNetwork(MLPClassifier, Chromosome):

    # ******************************************************************************
    # Neural Network methods
    # ******************************************************************************
    
    def __init__(self, arquitecture = select_arquitecture(), learning_rate = select_learning_rate(), variables = []):
        self.selected_arquitecture = arquitecture
        self.selected_learning_rate = learning_rate
        self.selected_variables = variables

        self.predictions = []
        self.accuracy = 0

        # MLP Classifier init
        # http://scikit-learn.org/stable/modules/generated/sklearn.neural_network.MLPClassifier.html
        MLPClassifier.__init__(
            self,
            hidden_layer_sizes = tuple(self.selected_arquitecture),
            learning_rate = 'constant',
            learning_rate_init = self.selected_learning_rate,
        )
    
    def do_train(self, X_train, y_train):
        variables_to_drop = []
        for i in range(0, len(X_train.columns)):
            if i not in self.selected_variables:
                variables_to_drop.append(i)
            
        new_X_train = X_train.drop(X_train.columns[variables_to_drop], axis = 1)
        self.fit(new_X_train, y_train)

    def do_classify(self, X_test):
        variables_to_drop = []
        for i in range(0, len(X_test.columns)):
            if i not in self.selected_variables:
                variables_to_drop.append(i)

        new_X_test = X_test.drop(X_test.columns[variables_to_drop], axis = 1)
        self.predictions = self.predict(new_X_test)

    def do_evaluate_accuracy(self, y_test):
        self.accuracy = accuracy_score(y_test, self.predictions)

    # ******************************************************************************
    # Chromosome methods
    # ******************************************************************************

    def get_fitness(self):
        return self.accuracy

    def get_genes(self):
        # TODO: implement selected variables
        genes = (self.selected_variables, self.selected_arquitecture, self.selected_learning_rate)
        return genes

    def prepare_fitness(self, X_train, y_train):
        if self.accuracy != 0: return
        self.do_train(X_train, y_train)

    def calculate_fitness(self, X_test, y_test):
        if self.accuracy != 0: return
        self.do_classify(X_test)
        self.do_evaluate_accuracy(y_test)

    # Crossover methods
    def crossover_children(self, chromosome):
        variables = chromosome.get_genes()[0]
        arquitecture = chromosome.get_genes()[1]
        learning_rate = chromosome.get_genes()[2]
        v1, v2 = self.cross_variables(variables)
        a1, a2 = self.cross_arquitecture(arquitecture)
        l1, l2 = self.cross_learning_rate(learning_rate)

        children_one = NeuralNetwork.instantiate_with_attributes(v1, a1, l1)
        children_two = NeuralNetwork.instantiate_with_attributes(v2, a2, l2)
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
    
    def cross_learning_rate(self, learning_rate):
        if randint(0, 100) <= LEARNING_RATE_PROBABILITY:
            return learning_rate, self.selected_learning_rate
        else:
            return self.selected_learning_rate, learning_rate

    def mutate(self, mutation_rate):
        # TODO: do this
        pass

    # ******************************************************************************
    # Static methods
    # ******************************************************************************

    @staticmethod
    # instantiate with random parameters
    # used to create the first generation of neural network population
    def instantiate():
        variables = select_variables()
        ann = NeuralNetwork(variables= variables)
        return ann


    @staticmethod
    def instantiate_with_attributes(variables, arquitecture, learning_rate):
        ann = NeuralNetwork(
            variables = variables,
            arquitecture = arquitecture,
            learning_rate = learning_rate
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

