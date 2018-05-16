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

    def mutate(self, mutation_rate):
        # TODO: do this
        pass

class Population:

    def __init__(self, size):
        self.chromosomes = []
    
    def get_chromosomes(self):
        return self.chromosomes

    def add_chromosome(self, chromosome):
        self.chromosomes.append(chromosome)

class GeneticAlgorithm:
    @staticmethod
    def evolve(population):
        pass
    
    @staticmethod
    def crossover(population):
        # TODO: add select tournament
        population.get_chromosomes().sort(key=lambda ann: ann.get_fitness(), reverse = True)
        crossover_population = Population(0)
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
                elite_chromosome_one,
                elite_chromosome_two
            )
            crossover_population.add_chromosome(new_chromosome)
            i += 1
        return crossover_population

    @staticmethod
    def crossover_chromosomes(chromosome_one, chromosome_two):
        # TODO: do this
        return Chromosome.instantiate()

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


        


