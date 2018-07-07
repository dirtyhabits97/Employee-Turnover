from settings import POPULATION_SIZE

class Population:
    def __init__(self):
        self.chromosomes = []
    
    def get_chromosomes(self):
        return self.chromosomes

    def get_size(self):
        return len(self.chromosomes)

    def get_best_chromosome(self):
        return self.chromosomes[0]

    def add_chromosome(self, new_c):
        idx = self.get_size()
        for i in range(self.get_size()):
            if new_c.get_fitness() > self.chromosomes[i].get_fitness():
                idx = i
                break
        self.chromosomes[idx:idx] = [new_c]

    def calculate_fitness(self, X, y):
        for c in self.chromosomes:
            c.calculate_fitness(X, y)

    # ******************************************************************************
    # Helper methods
    # ******************************************************************************

    # Helper method for printing
    def get_max_chromosome_length(self):
        max_length = max (len(c) for c in self.get_chromosomes())
        return max_length

    # ******************************************************************************
    # Static methods
    # ******************************************************************************

    @staticmethod
    def instantiate(new_chromosome):
        p = Population()
        while p.get_size() != POPULATION_SIZE:
            p.add_chromosome(new_chromosome())
        return p

            

    