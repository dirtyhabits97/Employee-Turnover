from random import random, randint
from util_methods import crossover_array

class Variable:
    def __init__(self, v):
        self.v = v

    def mutate(self, mutation_rate):
        for i in range(len(self.v)):
            if random() < mutation_rate:
                self.v[i] = 0 if self.v[i] == 1 else 1

    def crossover(self, var):
        return crossover_array(self, var)

    def raw(self):
        return self.v

    def __len__(self):
        return len(self.v)


class Arquitecture:
    def __init__(self, a):
        self.a = a

    def mutate(self, mutation_rate):
        from settings import MIN_NUMBER_OF_NODES as MIN, MAX_NUMBER_OF_NODES as MAX

        for i in range(len(self.a)):
            new_a = self.a[i]
            while new_a == self.a[i]:
                new_a = randint(MIN, MAX)
            self.a[i] = new_a

    def crossover(self, a):
        return crossover_array(self, a)

    def raw(self):
        return self.a