from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score
from util_methods import select_arquitecture, select_learning_rate

class NeuralNetwors:
    def __init__(self):
        self.selected_arquitecture = select_arquitecture()
        self.selected_learning_rate = select_learning_rate()

        # MLP Classifier init
        # http://scikit-learn.org/stable/modules/generated/sklearn.neural_network.MLPClassifier.html
        MLPClassifier.__init__(
            self,
            hidden_layer_sizes = tuple(self.selected_arquitecture),
            learning_rate = 'constant',
            learning_rate_init = self.selected_learning_rate,
        )
    

