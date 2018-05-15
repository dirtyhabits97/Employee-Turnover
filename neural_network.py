from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score
from util_methods import select_arquitecture, select_learning_rate

class NeuralNetwors(MLPClassifier):
    def __init__(self, variables):
        self.selected_arquitecture = select_arquitecture()
        self.selected_learning_rate = select_learning_rate()
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
    
    def do_train(self, input_vector, output_vector):
        self.fit(input_vector, output_vector)

    def do_classify(self, input_test):
        self.predictions = self.predict(input_test)

    def do_evaluate_accuracy(self, output_test):
        self.accuracy = accuracy_score(output_test, self.predictions)

