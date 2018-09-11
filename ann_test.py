from data.data_manager import DataManager

from settings import FILE_PATH
from settings import SCALE_EXCLUDE_VARIABLES
from settings import VARIABLES_TO_OH_ENCODE, VARIABLES_TO_B_ENCODE
from settings import VARIABLES_TO_DELETE
from settings import VARIABLE_TO_CLASSIFY

def setup_data_manager():
    data_manager = DataManager.shared()
    data_manager.read_data(FILE_PATH)
    # - Data preprocessing -
    # Scaling
    data_manager.scale_data(SCALE_EXCLUDE_VARIABLES)
    # Encoding
    data_manager.one_hot_encode_data(VARIABLES_TO_OH_ENCODE)
    data_manager.binary_encode_data(VARIABLES_TO_B_ENCODE)
    # Remove variables
    data_manager.drop_columns(VARIABLES_TO_DELETE)

    # - Data Split -
    data_manager.split_data(VARIABLE_TO_CLASSIFY)

def main():
    setup_data_manager()
    dm = DataManager.shared()
    # F = 3
    v1 = [1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0]
    # F >= 2
    v2 = [1, 1, 1, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0 ,0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0]

    # E1
    e1 = [1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1]
    # E2
    e2 = [1, 0, 1, 1, 0, 1, 0, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0]
    # E3
    e3 = [1, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0]

    from neural_network.neural_network import NeuralNetwork
    for i in range(10):
        # ann1 = NeuralNetwork(v1)
        # ann2 = NeuralNetwork(v2)

        # annE1 = NeuralNetwork(e1)
        # annE2 = NeuralNetwork(e2)
        # annE3 = NeuralNetwork(e3)

        X = dm.get_X_train()
        y = dm.get_y_train()
        # ann1.cross_val_train(X, y)
        # ann2.cross_val_train(X, y)

        # annE1.cross_val_train(X, y)
        # annE2.cross_val_train(X, y)
        # annE3.cross_val_train(X, y)

        from sklearn.model_selection import cross_val_score

        from sklearn.tree import DecisionTreeClassifier
        from sklearn.linear_model import LogisticRegression

        tree = DecisionTreeClassifier(random_state=0)
        logr = LogisticRegression()

        score_tree = cross_val_score(tree, X, y, cv=10)
        score_logr = cross_val_score(logr, X, y, cv=10)

        accuracy_tree = score_tree.mean()
        accuracy_logr = score_logr.mean()

        print("\n")
        print("Run #%i:" % i)
        # print("E1: ", annE1.get_accuracy())
        # print("E2: ", annE2.get_accuracy())
        # print("E3: ", annE3.get_accuracy())
        # print("\n")
        # print("F = 3: ", ann1.get_accuracy())
        # print("F >= 2: ", ann2.get_accuracy())

        print("Tree score: ", accuracy_tree)
        print("Logistic Regression score: ", accuracy_logr)
        print("\n")

if __name__ == '__main__':
    main()