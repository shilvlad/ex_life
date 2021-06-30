import cells
import world
import config


if __name__ == "__main__":
    w = world.World()

    print("Размер популяции:", w.get_world_size())
    for i in w.get_all_cellsA():
        print(i.get_position())

    print("Очистка популяции")
    w.clean_world()
    print("Размер популяции:", w.get_world_size())

    w.debug_print_world()
