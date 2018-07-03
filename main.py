from data_manager import DataManager

from settings import FILE_PATH, VARIABLE_TO_CLASSIFY
from settings import NUMBER_OF_GENERATIONS, TARGET_FITNESS

from print_methods import print_population

def setup_data_manager():
    data_manager = DataManager.shared()
    data_manager.read_data(FILE_PATH)
    data_manager.split_data(VARIABLE_TO_CLASSIFY)
    data_manager.print_data()

def setup_population():
    dm = DataManager.shared()

    from genetic_algorithm import Population
    from neural_network import NeuralNetwork

    population = Population.instantiate_population(NeuralNetwork.instantiate)
    population.calculate_fitness(dm.get_X_train(), dm.get_y_train())
    population.get_chromosomes().sort(key=lambda ann: ann.get_fitness(), reverse = True)
    print_population(population, 0)
    return population

def main():
    setup_data_manager()
    dm = DataManager.shared()

    from genetic_algorithm import GeneticAlgorithm

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
