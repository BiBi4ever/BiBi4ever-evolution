# -*- coding: utf-8 -*-
import random
import logging
import os
import time
from grid import *

# Параметры
length = 20 # длина цепочки ДНК
population_size = 20 # размер популяции
generations = 3 # количество поколений
population_mutation = 1.0 # шанс мутации индивида внутри популяции
number_mutations = 1 # Количество мутаций за итерацию

# ФУНКЦИИ

# Генерирование (прочитывание из файла) базовой популяции
def generate_DNA(length):
    DNA = ''.join(random.choice('CGTA') for _ in range(length)) # это с равными вероятностями для любого нуклеотида
    return DNA

# Мутирование строки
def mutate_DNA(DNA, number_mutations=1):
    DNA_list = [i for i in DNA] #перевод строки в лист т.к строки неизменяемы
    for _ in range(number_mutations):
        DNA_list[random.randrange(len(DNA_list))] = random.choice('ATGC') #выбираем рандомный индекс в созданном выше листе и заменяем на рандомну
    return ''.join(DNA_list)


# Получение признаков/ прочитывание генов (подсчет % GC)
def calculate_GC(DNA):
    return (DNA.count('G') + DNA.count('C'))/(len(DNA))

# Отбор (GC < 0.4)
def selection(population, GC_threshold=0.4):
    population_selected = [creature for creature in population if calculate_GC(creature) >= GC_threshold]
    return population_selected

# Размножение/рекомбинация
def multiply_population(population, length=length):
    # primitiva recoimbination
    for _ in range(len(population)):
        parents = population[_ : _ + 2]
        child = parents[0][0:length//2] + parents[1][length//2::]
        population.append(child)
    return population

# ЭВОЛЮЦИЯ
outfile_dir = os.path.dirname(__file__)
outfile_name = 'output.txt'
outfile_path = os.path.join(outfile_dir, outfile_name)
outfile = open(outfile_name, 'wt')

logging.basicConfig(filename="evolution.log",
                    format='%(asctime)s %(levelname)-8s %(message)s',
                    level=logging.INFO,
                    datefmt='%Y-%m-%d %H:%M:%S')

#logging.info("Outfile has been opened")
# Генерирование (прочитывание из файла) базовой популяции

#outfile.write("Generating base population" + "\n")
population_list = [generate_DNA(length) for _ in range(population_size)]
population_selected = population_list

print("Generated empty grid")
time.sleep(1)
grid = Grid((30, 30))

coords = [x for x in itertools.product(range(grid.width), range(grid.height))]
coords = random.sample(coords, population_size)

grid.display()
time.sleep(2)

print("Populating the grid...")
time.sleep(1)
grid.populate(coords)
grid.display()
time.sleep(2)

for _ in range(generations):
    # Мутация
    population_mutated = [mutate_DNA(creature) for creature in population_selected]
    # Отбор
    population_selected = [creature for creature in population_mutated if calculate_GC(creature) >= 0.6]
    population_new = multiply_population(population_selected)
    population_selected = [creature for creature in population_new if calculate_GC(creature) >= 0.6]
    population_size = len(population_selected)
    if population_size > grid.capacity:
        print("Population overflow!")
        break

    coords = [x for x in itertools.product(range(7), range(7))]
    live_cells = random.sample(coords, population_size)

    if len(live_cells) == 0:
        print("All cells died!")
        break

    grid.populate(live_cells)
    # Размножение
    print("Generation # %d"  % _)
    time.sleep(1)
    grid.display()
    time.sleep(2)

print("Your population survived the toll of %d generations!" % generations)

# Закрываем файл
#outfile.close()
#logging.info("Outfile has been closed. File path is " + outfile_path)
