# ******************************************************************************
# Neural Network settings
# ******************************************************************************

MAX_NUMBER_OF_VARIABLES     = 12
MIN_NUMBER_OF_VARIABLES     = 8
MAX_NUMBER_OF_LAYERS        = 3
MIN_NUMBER_OF_LAYERS        = 1
MAX_NUMBER_OF_NODES         = 9
MIN_NUMBER_OF_NODES         = 5


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

# Data set retrieved from: https://www.kaggle.com/pavansubhasht/ibm-hr-analytics-attrition-dataset
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
                                    "OverTime",
                                    "Over18"
                                ]
VARIABLES_TO_DELETE         =   [
                                    "EmployeeNumber",
                                    "EmployeeCount",
                                    "Over18",
                                    "DailyRate",
                                    "HourlyRate",
                                    "MonthlyRate",
                                    "StandardHours"
                                ]
SCALE_EXCLUDE_VARIABLES       = [
                                    "BusinessTravel",
                                    "Department",
                                    "EducationField",
                                    "JobRole",
                                    "MaritalStatus",
                                    "Gender",
                                    "OverTime",
                                    "Over18",
                                    "EmployeeNumber",
                                    "Attrition",
                                    "Education",
                                    "EnvironmentSatisfaction",
                                    "JobInvolvement",
                                    "JobLevel",
                                    "JobSatisfaction",
                                    "StockOptionLevel",
                                    "WorkLifeBalance",
                                    "RelationshipSatisfaction"
                                ]
BINARY_ENCODING_DICTIONARY  =   { 
                                    "Gender": { "No": 0, "Yes": 1 },
                                    "Over18": { "N": 0, "Y": 1 },
                                    "OverTime": { "No": 0, "Yes": 1 }
                                }
