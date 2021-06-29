import config
import cells

class World():

    def __init__(self):
        self.population = []
        for i in range(config.WORLD_POPULATION_CELLS_A):
            self.population.append(cells.CellA())

    def add_cellA(self, x, y):
        tmpCell = cells.CellA(x=x, y=y)
        self.population.append(tmpCell)
        return tmpCell


    def get_world_size(self):
        return len(self.population)

    def get_all_cellsA(self):
        return self.population

    def clean_world(self):
        uniqueList = []
        for item in self.population:
            itemExist = False
            for x in uniqueList:
                if x == item:
                    itemExist = True
                    break
            if not itemExist:
                uniqueList.append(item)
        print(uniqueList)





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






