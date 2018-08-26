from data.data_manager import DataManager

from settings import FILE_PATH
from settings import VARIABLE_TO_CLASSIFY, VARIABLES_TO_DELETE
from settings import VARIABLES_TO_OH_ENCODE, VARIABLES_TO_B_ENCODE
from settings import NUMBER_OF_GENERATIONS, TARGET_FITNESS

from helper_methods.print_methods import print_population

def setup_data_manager():
    data_manager = DataManager.shared()
    data_manager.read_data(FILE_PATH)
    data_manager.drop_columns(VARIABLES_TO_DELETE)
    data_manager.one_hot_encode_data(VARIABLES_TO_OH_ENCODE)
    data_manager.binary_encode_data(VARIABLES_TO_B_ENCODE)
    data_manager.split_data(VARIABLE_TO_CLASSIFY)
    data_manager.rfe_feature_selection(15)
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

    # from genetic_algorithm.genetic_algorithm import GeneticAlgorithm

    # population = setup_population()
    # generation_number = 1

    # while generation_number != NUMBER_OF_GENERATIONS and population.get_chromosomes()[0].get_fitness() < TARGET_FITNESS:
    #     population = GeneticAlgorithm.evolve(population)
    #     population.calculate_fitness(dm.get_X_train(), dm.get_y_train())
    #     population.get_chromosomes().sort(key=lambda ann: ann.get_fitness(), reverse = True)
    #     print_population(population, generation_number)
    #     generation_number += 1

if __name__ == '__main__':
    main()
