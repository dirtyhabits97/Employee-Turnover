import numpy as np

def print_variables(data_frame):
    output = ""
    max_name_len = max(len(col) for col in data_frame)
    for i, col in enumerate(data_frame):
        added_str = " " * (max_name_len - len(col))
        output += "X%02d: %s%s %s" % (i, col, added_str, data_frame[col].dtype.name)
        output += "\n"

    line_len = len(output.split("\n")[0])
    title = "(VARIABLES)"
    decoration = "=" * int((line_len + 4 - len(title))/2)
    header = decoration + title + decoration
    footer = "=" * len(header)

    print(header)
    print("\n" + output)
    print(footer)

def print_population(population, gen_number):
    header_title = "Generation #" + str(gen_number) + "| Fittest chromosome fitness: " + str(population.get_best_chromosome().get_fitness())
    header_frame = "\n" + "*" * len(str(header_title))

    max_length = population.get_max_chromosome_length()
    output = ""
    i = 0
    for ann in population.get_chromosomes():
        c_length = max_length - len(ann)
        added_length = " " * c_length
        output += "Chromosome " 
        output +=  str(i).zfill(2) 
        output += ": "
        output += str(ann)
        output += added_length
        output += "| Fitness:  "
        output += format(ann.get_fitness(), '.10f')
        output += "\n"
        i += 1

    header_frame = "*" * len(output.split("\n")[0])
    padding = " " * int((len(header_frame) - len(header_title))/ 2)
    header_title = padding + header_title
    print(header_frame, "\n")
    print(header_title, "\n")
    print(header_frame)
    print(output)
