from genetic_algorithm.population import Population
from settings import NUMBER_OF_ELITE_CHROMOSOMES, POPULATION_SIZE, MUTATION_RATE, TOURNAMENT_POPULATION

class GeneticAlgorithm:
    # TODO: probar metodos de seleccion
    @staticmethod
    def evolve(population):
        crossover_population = GeneticAlgorithm.crossover(population)
        mutated_population   = GeneticAlgorithm.mutate(crossover_population)
        return mutated_population

    @staticmethod
    def crossover(population):
        p = Population()

        # Select the elite chromosomes aka chromosomes with highest fitness
        for i in range(NUMBER_OF_ELITE_CHROMOSOMES):
            elite_c = population.get_chromosomes()[i]
            p.add_chromosome(elite_c)

        # Exclude elite chromosomes
        # Re-create the rest of the population
        while p.get_size() != POPULATION_SIZE:
            # Get best chromosomes from 2 tournaments
            c1 = GeneticAlgorithm.selection_method(population)
            c2 = GeneticAlgorithm.selection_method(population)

            # Apply crossover to the chromosomes
            new_c1, new_c2 = GeneticAlgorithm.crossover_chromosomes(c1, c2)

            # Add the new chromosomes to the population
            p.add_chromosome(new_c1)
            if p.get_size() != POPULATION_SIZE:
                p.add_chromosome(new_c2)

        return p

    @staticmethod
    def crossover_chromosomes(c1, c2):
        return c1.crossover_with(c2)

    @staticmethod
    def mutate(population):
        # Exclude the elite chromosomes
        for i in range(NUMBER_OF_ELITE_CHROMOSOMES, POPULATION_SIZE):
            c = population.get_chromosomes()[i]
            GeneticAlgorithm.mutate_chromosome(c)
        return population

    @staticmethod
    def mutate_chromosome(chromosome):
        chromosome.mutate(MUTATION_RATE)

    @staticmethod
    def selection_method(population):
        return GeneticAlgorithm.select_tournament(population)

    @staticmethod
    def select_tournament(population):
        from random import randint

        selected_population = Population()
        for _ in range(0, TOURNAMENT_POPULATION):
            c = population.get_chromosomes()[randint(0, POPULATION_SIZE - 1)]
            selected_population.add_chromosome(c)
        
        # Return the best chromosome from the population
        return selected_population.get_best_chromosome()