import random
import config

# Общий класс клетки
class Cell:
    def __init__(self, x = random.randint(0, config.WORLD_SIZE_X - 1), y= random.randint(0, config.WORLD_SIZE_Y - 1)):
        self.x = x
        self.y = y

    def __hash__(self):
        return hash(self.x) + hash(self.y)

    def get_position(self):
        return self.x, self.y

    def __eq__(self, other):
        if self.x == other.x and self.y == other.y:
            return True
        else:
            return False


# Класс клетки типа А
class CellA(Cell):
    def __init__(self, x = random.randint(0, config.WORLD_SIZE_X - 1), y= random.randint(0, config.WORLD_SIZE_Y - 1)):
        super().__init__(x,y)


