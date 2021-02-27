import random

class Creature:
    def __init__(self, DNA_length=20):
        self.DNA_length = DNA_length
        self.DNA = ''.join(random.choice('CGTA') for _ in range(DNA_length))
        self.status = 1 # 0 - dead 1 - alive
        self.GC = (self.DNA.count('G') + self.DNA.count('C'))/(self.DNA_length)

    def mutate_DNA(self, number_mutations=1):
        DNA_list = [i for i in self.DNA] #перевод строки в лист т.к строки неизменяемы
        for _ in range(number_mutations):
            DNA_list[random.randrange(len(DNA_list))] = random.choice('ATGC') #выбираем рандомный индекс в созданном выше листе и заменяем на рандомну
            self.DNA = ''.join(DNA_list)
        self.GC = (self.DNA.count('G') + self.DNA.count('C'))/(self.DNA_length)

    def evaluate(self, GC_threshold=0.4):
        if self.GC < GC_threshold:
            self.status = 0


class Population:
    def __init__(self, population_size=20, criteria_threshold=0.4):
        self.population_size = population_size
        self.population = []
        self.criteria_threshold = criteria_threshold

    def initiate(self, population_size=20):
        self.population = [Creature() for _ in range(20)]

    def mutate(self):
        if len(self.population) == 0:
            print("There is nothing to mutate!")
        for c in self.population:
            c.mutate_DNA()

    def select(self):
        for c in self.population:
            c.evaluate()
        self.population_size = len(self.population)


x = Population()
y = Creature()
y.mutate_DNA()
y.evaluate()
print(y.status)

x.initiate()
print(x.population_size)
x.mutate()
x.select()
print(x.population_size)
