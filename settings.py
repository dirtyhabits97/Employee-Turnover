# ******************************************************************************
# Neural Network settings
# ******************************************************************************

MAX_NUMBER_OF_VARIABLES     = 10
MIN_NUMBER_OF_VARIABLES     = 5
MAX_NUMBER_OF_LAYERS        = 4
MIN_NUMBER_OF_LAYERS        = 1
MAX_NUMBER_OF_NODES         = 10
MIN_NUMBER_OF_NODES         = 3
MAX_LEARNING_RATE           = 0.005
MIN_LEARNING_RATE           = 0.001
LEARNING_RATE_PROBABILITY   = 25


# ******************************************************************************
# Genetic Algorithm settings
# ******************************************************************************

NUMBER_OF_GENERATIONS       = 1000
POPULATION_SIZE             = 20
NUMBER_OF_ELITE_CHROMOSOMES = int(POPULATION_SIZE * 0.5) # 10% del tamaño de la población
MUTATION_RATE               = 0.01
TARGET_FITNESS              = 1.01

# ******************************************************************************
# Data Manager settings
# ******************************************************************************

FILE_PATH                   = "/Users/gonzalo/Desktop/turnover_dataset.csv"
VARIABLE_TO_CLASSIFY        = "Attrition"

# ******************************************************************************
# Debug settings
# ******************************************************************************

from enum import Enum
class OrderedEnum(Enum):
    def __ge__(self, other):
        if self.__class__ is other.__class__:
            return self.value >= other.value
        return NotImplemented
    def __gt__(self, other):
        if self.__class__ is other.__class__:
            return self.value > other.value
        return NotImplemented
    def __le__(self, other):
        if self.__class__ is other.__class__:
            return self.value <= other.value
        return NotImplemented
    def __lt__(self, other):
        if self.__class__ is other.__class__:
            return self.value < other.value
        return NotImplemented

class Log(OrderedEnum):
    no_logs = 0
    show_highest_fitness = 1
    show_chromosome_fitness = 2
    show_variable_report = 3
    show_predictions = 4
    show_learning_process = 5

LOG_LEVEL = Log.show_chromosome_fitness
