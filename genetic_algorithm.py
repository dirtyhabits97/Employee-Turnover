from random import randint, random

from settings import POPULATION_SIZE, NUMBER_OF_ELITE_CHROMOSOMES, MUTATION_RATE, TOURNAMENT_POPULATION

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
        pass

    def crossover_children(self, chromosome):
        pass

    def calculate_fitness(self):
        pass

    def __str___(self):
        return self.genes.__str__()


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

    def get_size(self):
        return len(self.get_chromosomes())

    def add_chromosome(self, chromosome):
        self.chromosomes.append(chromosome)

    def instantiate_chromosome(self):
        return self.instantiate()

    def calculate_fitness(self, X, y):
        for chromosome in self.get_chromosomes():
            chromosome.calculate_fitness(X, y)

    def __len__(self):
        return len(self.get_chromosomes())

    def max_chromosome_length(self):
        max_length = max (len(c) for c in self.get_chromosomes())
        return max_length

    # If there are multiple chromosomes with the same fitness it picks the fitst one
    def best_fitness_chromosome(self):
        best_idx = 0
        best_fitness = 0
        for i in range(1, self.get_size()):
            c = self.get_chromosomes()[i]
            if c.get_fitness() > best_fitness:
                best_idx = i
                best_fitness = c.get_fitness()
        return self.get_chromosomes()[best_idx]


class GeneticAlgorithm:
    @staticmethod
    def evolve(population):
        crossover_population = GeneticAlgorithm.crossover(population)
        mutated_population = GeneticAlgorithm.mutate(crossover_population)
        return mutated_population
        # return crossover_population
    
    @staticmethod
    def crossover(population):
        print("Doing cross over")
        # TODO: add select tournament
        population.get_chromosomes().sort(key=lambda ann: ann.get_fitness(), reverse = True)
        crossover_population = Population()
        for i in range(NUMBER_OF_ELITE_CHROMOSOMES):
            elite_chromosome = population.get_chromosomes()[i]
            crossover_population.add_chromosome(elite_chromosome)

        # exclude elite chromosomes
        while len(crossover_population) != POPULATION_SIZE:
            print("Before tournament")
            chromosome_one = GeneticAlgorithm.select_tournament(population)
            chromosome_two = GeneticAlgorithm.select_tournament(population)

            print("Making new chromosomes")
            new_chromosome_one, new_chromosome_two = GeneticAlgorithm.crossover_chromosomes(
                population,
                chromosome_one,
                chromosome_two
            )
            print("Finished making new chromosomes")
            crossover_population.add_chromosome(new_chromosome_one)
            if len(crossover_population) != POPULATION_SIZE:
                crossover_population.add_chromosome(new_chromosome_two)

        print("Crossover is over")

        return crossover_population

    @staticmethod
    def crossover_chromosomes(population, chromosome_one, chromosome_two):
        crossover_chromosome_one, crossover_chromosome_two = chromosome_one.crossover_children(chromosome_two)
        return crossover_chromosome_one, crossover_chromosome_two

    @staticmethod
    def mutate(population):
        # excluir los cromosomas elite
        for i in range(NUMBER_OF_ELITE_CHROMOSOMES, POPULATION_SIZE):
            chromosome = population.get_chromosomes()[i]
            GeneticAlgorithm.mutate_chromosome(chromosome)
        return population
    
    @staticmethod
    def mutate_chromosome(chromosome):
        chromosome.mutate(chromosome, MUTATION_RATE)

    @staticmethod
    def select_tournament(population):
        print("Tournament going on")
        selected_population = Population()
        for _ in range(0, TOURNAMENT_POPULATION):
            c = population.get_chromosomes()[randint(0, POPULATION_SIZE - 1)]
            selected_population.add_chromosome(c)
        return selected_population.best_fitness_chromosome()