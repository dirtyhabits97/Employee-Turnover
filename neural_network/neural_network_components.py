from random import random, randint
from helper_methods.util_methods import crossover_array

class Variable:
    def __init__(self, v):
        self.v = v

    def mutate(self, mutation_rate):
        for i in range(len(self.v)):
            if random() < mutation_rate:
                self.v[i] = 0 if self.v[i] == 1 else 1

    def crossover_with(self, v):
        return crossover_array(self.raw(), v.raw())

    def raw(self):
        return self.v

    def used_variables(self):
        used = []
        for i in range(len(self)):
            if self.v[i] == 1:
                used.append(i)
        return used

    def unused_variables(self):
        unused = []
        for i in range(len(self)):
            if self.v[i] == 0:
                unused.append(i)
        return unused

    def __len__(self):
        return len(self.v)


class Arquitecture:
    def __init__(self, a):
        self.a = a

    def mutate(self, mutation_rate):
        from settings import MIN_NUMBER_OF_NODES as MIN, MAX_NUMBER_OF_NODES as MAX

        if random() > mutation_rate: return

        for i in range(len(self.a)):
            new_a = self.a[i]
            while new_a == self.a[i]:
                new_a = randint(MIN, MAX)
            self.a[i] = new_a

    def crossover_with(self, a):
        return crossover_array(self.raw(), a.raw())

    def raw(self):
        return self.a