import cells
import world


if __name__ == "__main__":
    w = world.World()
    print(w.get_world_size())
    for i in w.get_all_cellsA():
        print(i.get_position())
    w.debug_print_world()
