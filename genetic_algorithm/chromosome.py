class Chromosome:
    def __init__(self):
        self.genes = []
        self.fitness = 0

    @staticmethod
    def instantiate():
        return Chromosome()

    def get_fitness(self):
        return self.fitness

    def get_genes(self):
        return self.genes

    def mutate(self, mutation_rate):
        for g in self.genes:
            g.mutate(mutation_rate)

    def crossover_children(self, chromosome):
        # Override this method
        pass

    def calculate_fitness(self):
        # Override this method
        pass

    def __str___(self):
        return self.genes.__str__()