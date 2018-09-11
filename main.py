from data.data_manager import DataManager

from settings import FILE_PATH
from settings import VARIABLE_TO_CLASSIFY, VARIABLES_TO_DELETE
from settings import VARIABLES_TO_OH_ENCODE, VARIABLES_TO_B_ENCODE
from settings import NUMBER_OF_GENERATIONS, TARGET_FITNESS
from settings import SCALE_EXCLUDE_VARIABLES

from helper_methods.print_methods import print_population

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

    # - Data Analysis
    # Recursive feature elimination
    data_manager.rfe_analysis(12)
    # PCA analysis
    data_manager.pca_analysis(0.95)

    # - Print Data -
    data_manager.print_variables()

def setup_population():
    dm = DataManager.shared()

    from genetic_algorithm.population import Population
    from neural_network.neural_network import NeuralNetwork

    population = Population.instantiate(NeuralNetwork.instantiate)
    population.calculate_fitness(dm.get_X_train(), dm.get_y_train())
    population.get_chromosomes().sort(key=lambda ann: ann.get_fitness(), reverse = True)
    print_population(population, 0)
    return population

def main():
    setup_data_manager()
    dm = DataManager.shared()
    from genetic_algorithm.genetic_algorithm import GeneticAlgorithm

    population = setup_population()
    generation_number = 1

    while generation_number != NUMBER_OF_GENERATIONS and population.get_chromosomes()[0].get_fitness() < TARGET_FITNESS:
        population = GeneticAlgorithm.evolve(population)
        population.calculate_fitness(dm.get_X_train(), dm.get_y_train())
        population.get_chromosomes().sort(key=lambda ann: ann.get_fitness(), reverse = True)
        print_population(population, generation_number)
        generation_number += 1

if __name__ == '__main__':
    main()
