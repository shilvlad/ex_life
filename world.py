import config
import cells

class World():
    population = []

    def __init__(self):
        for i in range(config.WORLD_POPULATION_CELLS_A):
            self.population.append(cells.CellA())


    def get_world_size(self):
        return len(self.population)

    def get_all_cellsA(self):
        return self.population

    def clean_world(self):
        pass


    def debug_print_world(self):
        pm = []
        for y in range (config.WORLD_SIZE_Y):
            pm.append([])
            for x in range (config.WORLD_SIZE_X):
                pm[y].append('-')

        for i in self.population:
            pm[i.x][i.y] = 'X'

        for y in range (config.WORLD_SIZE_Y):
            for x in range (config.WORLD_SIZE_X):
                print(pm[x][y], end='')
            print()






