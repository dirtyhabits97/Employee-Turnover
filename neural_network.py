from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score
from util_methods import select_arquitecture, select_learning_rate
from genetic_algorithm import Chromosome

class NeuralNetwork(MLPClassifier, Chromosome):

    # ******************************************************************************
    # Neural Network methods
    # ******************************************************************************
    
    def __init__(self):
        self.selected_arquitecture = select_arquitecture()
        self.selected_learning_rate = select_learning_rate()
        # self.selected_variables = variables

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
        self.fit(X_train, y_train)

    def do_classify(self, X_test):
        self.predictions = self.predict(X_test)

    def do_evaluate_accuracy(self, y_test):
        self.accuracy = accuracy_score(y_test, self.predictions)

    # ******************************************************************************
    # Chromosome methods
    # ******************************************************************************

    def get_fitness(self):
        return self.accuracy

    def get_genes(self):
        return self.selected_arquitecture

    def prepare_fitness(self, X_train, y_train):
        if self.accuracy != 0: return
        self.do_train(X_train, y_train)

    def calculate_fitness(self, X_test, y_test):
        self.do_classify(X_test)
        self.do_evaluate_accuracy(y_test)

    def crossover_children(self, chromosome):
        # TODO: do this
        pass

    def mutate(self, mutation_rate):
        # TODO: do this
        pass

    # ******************************************************************************
    # Static methods
    # ******************************************************************************

    @staticmethod
    def instantiate():
        # TODO: do this
        pass

