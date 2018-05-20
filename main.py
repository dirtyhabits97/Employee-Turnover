from data_manager import DataManager

FILE_PATH = "/Users/gonzalo/Desktop/turnover_dataset.csv"
VARIABLE_TO_CLASSIFY = "Attrition"
TARGET_FITNESS = 1.01
NUMBER_OF_GENERATIONS = 3

def print_population(pop, gen_number):
    max_length = pop.max_chromosome_length()
    print("\n-----------------------------------------------------")
    print("Generation #", gen_number, "| Fittest chromosome fitness: ", pop.get_chromosomes()[0].get_fitness())
    print("\n-----------------------------------------------------")
    i = 0
    for ann in pop.get_chromosomes():
        c_length = max_length - len(ann)
        added_length = " " * c_length
        print("Chromosome ", str(i).zfill(2), " :", ann, added_length, "| Fitness:  ", ann.get_fitness())
        i += 1

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
    population.prepare_fitness(dm.get_X_train(), dm.get_y_train())
    population.calculate_fitness(dm.get_X_test(), dm.get_y_test())
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
        population.prepare_fitness(dm.get_X_train(), dm.get_y_train())
        population.calculate_fitness(dm.get_X_test(), dm.get_y_test())
        population.get_chromosomes().sort(key=lambda ann: ann.get_fitness(), reverse = True)
        print_population(population, generation_number)
        generation_number += 1

if __name__ == '__main__':
    main()
