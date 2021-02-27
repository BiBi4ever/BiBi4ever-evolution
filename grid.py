import random
import itertools

class Grid:
    """docstring for Grid."""

    def __init__(self, size=(10,10)):
        self.size = size
        self.width, self.height = size
        self.capacity = self.width * self.height
        self.string = [["." for _ in range(self.width)] for _ in range(self.height)]

    def empty(self):
        self.string = [["." for _ in range(self.width)] for _ in range(self.height)]

    def from_file(self, file):
        population_file = open(file, "rt")
        grid = []
        for line in population_file.readlines():
            row = list(line.split()[0])
            grid.append(row)
        population_file.close()
        self.string = grid

    def display(self):
        output = ""
        for row in self.string:
             line = " ".join(row)
             output += line + "\n"
        print(output)

    def populate(self, live_cells):
        self.string = [["." for _ in range(self.width)] for _ in range(self.height)]
        for coord in live_cells:
            self.string[coord[0]][coord[1]] = "*"

    def repopulate(self):
        coords = [x for x in itertools.product(range(10), range(10))]
        coords = random.sample(coords, 20)
        for coord in coords:
            self.string[coord[0]][coord[1]] = "*"
