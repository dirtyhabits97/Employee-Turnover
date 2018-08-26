# ******************************************************************************
# Neural Network settings
# ******************************************************************************

MAX_NUMBER_OF_VARIABLES     = 10
MIN_NUMBER_OF_VARIABLES     = 5
MAX_NUMBER_OF_LAYERS        = 4
MIN_NUMBER_OF_LAYERS        = 1
MAX_NUMBER_OF_NODES         = 10
MIN_NUMBER_OF_NODES         = 3


# ******************************************************************************
# Genetic Algorithm settings
# ******************************************************************************

from math import ceil

NUMBER_OF_GENERATIONS       = 1000
POPULATION_SIZE             = 25 # Echegaray-Calderon, O A Barrios-Aranibar, D
NUMBER_OF_ELITE_CHROMOSOMES = ceil(POPULATION_SIZE * 0.1)# Echegaray-Calderon, O A Barrios-Aranibar, D
MUTATION_RATE               = 0.01
TARGET_FITNESS              = 1.01
TOURNAMENT_POPULATION       = ceil(POPULATION_SIZE * 0.2)

# ******************************************************************************
# Data Manager settings
# ******************************************************************************

FILE_PATH                   = "/Users/gonzalo/Desktop/turnover_dataset.csv"
VARIABLE_TO_CLASSIFY        = "Attrition"
VARIABLES_TO_OH_ENCODE      =   [
                                    "BusinessTravel",
                                    "Department",
                                    "EducationField",
                                    "JobRole",
                                    "MaritalStatus"
                                ]
VARIABLES_TO_B_ENCODE       =   [
                                    "Gender",
                                    "OverTime"
                                ]
VARIABLES_TO_DELETE         =   [
                                    "EmployeeNumber",
                                    "Over18",
                                    "DailyRate",
                                    "HourlyRate",
                                    "MonthlyRate",
                                    "StandardHours"
                                ]
BINARY_ENCODING_DICTIONARY  =   { 
                                    "Gender": { "No": 0, "Yes": 1 },
                                    "Over18": { "N": 0, "Y": 1 },
                                    "OverTime": { "No": 0, "Yes": 1 }
                                }

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

LOG_LEVEL = Log.show_variable_report
