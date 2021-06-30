import unittest
import world, cells
import config


class TestWorld(unittest.TestCase):

    def setUp(self) -> None:
        self.w = world.World()

    def test_add_cellA(self):
        self.assertEqual(self.w.add_cellA(2,2), cells.CellA(2,2))
        self.assertNotEqual(self.w.add_cellA(2,2), cells.CellA(2,3))

    def test_get_world_size(self):
        self.assertEqual(self.w.get_world_size(), config.WORLD_POPULATION_CELLS_A)

    def test_get_all_cellsA(self):
        self.assertEqual(self.w.get_all_cellsA().__len__(), config.WORLD_POPULATION_CELLS_A)

    def test_clean_world(self):
        self.s = world.World()
        self.s.population.clear()
        self.s.add_cellA(2, 2)
        self.s.add_cellA(2, 2)
        self.s.add_cellA(2, 3)
        self.s.add_cellA(3, 2)
        self.s.clean_world()
        self.assertEqual(self.s.get_world_size(), 3)


if __name__ == '__main__':
    unittest.main()