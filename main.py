import cells
import world
import config


if __name__ == "__main__":
    w = world.World()

    print("Размер мира:", w.get_world_size())
    for i in w.get_all_cellsA():
        print(i.get_position())

    w.clean_world()
    w.debug_print_world()
