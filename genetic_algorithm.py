from random import randint, random

NUMBER_OF_ELITE_CHROMOSOMES = 2
POPULATION_SIZE = 20
MUTATION_RATE = 0.01

class Chromosome:
    def __init__(self):
        self.genes = []
        self.fitness = 0

    @staticmethod
    def instantiate():
        # TODO: override this
        chromosome = Chromosome()
        return chromosome

    def get_fitness(self):
        return self.fitness

    def get_genes(self):
        return self.genes

    def mutate(self, mutation_rate):
        # TODO: do this
        pass

    def crossover_children(self, chromosome):
        # TODO: do this
        pass

class Population:

    def __init__(self):
        self.chromosomes = []

    @staticmethod
    def instantiate_population(instantiate):
        population = Population()
        population.instantiate = instantiate
        while len(population.chromosomes) != POPULATION_SIZE:
            new_chromosome = population.instantiate_chromosome()
            population.add_chromosome(new_chromosome)
        return population

    def get_chromosomes(self):
        return self.chromosomes

    def add_chromosome(self, chromosome):
        self.chromosomes.append(chromosome)

    def instantiate_chromosome(self):
        return self.instantiate()
    
    def train(self):
        # TODO: do this
        pass

    def calculate_fitness(self):
        # TODO: do this
        pass


class GeneticAlgorithm:
    @staticmethod
    def evolve(population):
        crossover_population = GeneticAlgorithm.crossover(population)
        mutated_population = GeneticAlgorithm.mutate(crossover_population)
        return mutated_population
    
    @staticmethod
    def crossover(population):
        # TODO: add select tournament
        population.get_chromosomes().sort(key=lambda ann: ann.get_fitness(), reverse = True)
        crossover_population = Population()
        for i in range(NUMBER_OF_ELITE_CHROMOSOMES):
            elite_chromosome = population.get_chromosomes()[i]
            crossover_population.add_chromosome(elite_chromosome)

        i = NUMBER_OF_ELITE_CHROMOSOMES
        # excluir los cromosomas elites
        while i != POPULATION_SIZE:
            idx1 = randint(0, NUMBER_OF_ELITE_CHROMOSOMES - 1)
            idx2 = randint(0, NUMBER_OF_ELITE_CHROMOSOMES - 1)
            while idx1 == idx2:
                idx2 = randint(0, NUMBER_OF_ELITE_CHROMOSOMES - 1)
            
            elite_chromosome_one = crossover_population.get_chromosomes()[idx1]
            elite_chromosome_two = crossover_population.get_chromosomes()[idx2]

            new_chromosome = GeneticAlgorithm.crossover_chromosomes(
                population,
                elite_chromosome_one,
                elite_chromosome_two
            )
            crossover_population.add_chromosome(new_chromosome)
            i += 1
        return crossover_population

    @staticmethod
    def crossover_chromosomes(population, chromosome_one, chromosome_two):
        crossover_chromosome_one, crossover_chromosome_two = chromosome_one.crossover_children(chromosome_two)
        if crossover_chromosome_one.get_fitness() < crossover_chromosome_two.get_fitness():
            return crossover_chromosome_two
        else:
            return crossover_chromosome_one

    @staticmethod
    def mutate(population):
        # excluir los cromosomas elite
        for i in range(NUMBER_OF_ELITE_CHROMOSOMES, POPULATION_SIZE):
            chromosome = population.get_chromosomes()[i]
            GeneticAlgorithm.mutate_chromosome(chromosome)
        return population
    
    @staticmethod
    def mutate_chromosome(chromosome):
        # TODO: update fitness
        chromosome.mutate(MUTATION_RATE)
