import random
import config

# Общий класс клетки
class Cell():
    def __init__(self):
        self.x = random.randint(0, config.WORLD_SIZE_X - 1)
        self.y = random.randint(0, config.WORLD_SIZE_Y - 1)

    def get_position(self):
        return self.x, self.y


# Класс клетки типа А
class CellA(Cell):
    def __init__(self):
        super().__init__()


