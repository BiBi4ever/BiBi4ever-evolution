import random
from objects import Creature, Population
from utils import *


# Параметры
length = 20 # длина цепочки ДНК
population_size = 20 # размер популяции
generations = 10 # количество поколений
population_mutation = 1.0 # шанс мутации индивида внутри популяции
number_mutations = 1 # Количество мутаций за итерацию


# Инициация
population = Population.initial_population(population_size)
# Мутирование 
mutatated_population = population.mutate()


print(population_new)


'''

# ЭВОЛЮЦИЯ
# Генерирование (прочитывание из файла) базовой популяции
print("Generating base population")

population_list = [generate_DNA(length) for _ in range(population_size)]
population_selected = population_list
population_size = len(population_selected)
generation = 1

while population_size > 1:
    print("Generation # " + str(generation))
    print("Population size: " + str(population_size))
    # Скрещивание (мутация)
    population_mutated = [mutate_DNA(creature) for creature in population_selected]
    # Получение признаков/ прочитывание генов (подсчет % нуклеотидов)
    # Отбор на основе признаков/критериев (GC < 0.4)
    population_selected = selection(population_mutated, 0.6)
    population_new = multiply_population(population_selected)

    population_size = len(population_new)
    print("Population size: " + str(population_size))
    generation += 1

# Получение результатов работы И/ИЛИ визуализация
'''
