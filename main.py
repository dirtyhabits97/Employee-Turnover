from data_manager import DataManager
from genetic_algorithm import Population, GeneticAlgorithm
from neural_network import NeuralNetwork

FILE_PATH = ""
VARIABLE_TO_CLASSIFY = ""
TARGET_FITNESS = 0.80

def print_population(pop, gen_number):
    print("\n-----------------------------------------------------")
    print("Generation #", gen_number, "| Fittest chromosome fitness: ", pop.get_chromosomes()[0].get_fitness())
    print("\n-----------------------------------------------------")
    i = 0
    for ann in pop.get_chromosomes():
        print("Chromosome ", str(i).zfill(2), " :", ann, "| Fitness:  ", ann.get_fitness())
        i += 1

def setup_data_manager():
    data_manager = DataManager.shared()
    data_manager.read_data(FILE_PATH)
    data_manager.split_data(VARIABLE_TO_CLASSIFY)
    data_manager.print_data()

def setup_population():
    dm = DataManager.shared()
    population = Population.instantiate_population(NeuralNetwork.instantiate)
    population.prepare_fitness(dm.get_X_train(), dm.get_y_train())
    population.calculate_fitness(dm.get_X_test(), dm.get_y_test())
    print_population(population, 0)
    return population

def main():
    setup_data_manager()
    dm = DataManager.shared()

    population = setup_population()
    generation_number = 1

    while population.get_chromosomes()[0].get_fitness < TARGET_FITNESS:
        population = GeneticAlgorithm.evolve(population)
        population.prepare_fitness(dm.get_X_train(), dm.get_y_train())
        population.calculate_fitness(dm.get_X_test(), dm.get_y_test())
        population.get_chromosomes().sort(key=lambda ann: ann.get_fitness(), reverse = True)
        print_population(population, generation_number)
        generation_number += 1

if __name__ == '__main__':
    main()
