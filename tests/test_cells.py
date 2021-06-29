import unittest
import cells

class TestCell(unittest.TestCase):

# Тест совпадения "==" двух клеток
    def test___eq__(self):
        c1 = cells.Cell(x=1, y=2)
        c2 = cells.Cell(x=1, y=2)
        c3 = cells.Cell(x=1, y=1)
        self.assertTrue(c1 == c2)
        self.assertFalse(c2 == c3)
        self.assertFalse(c1 == c3)

# Тест получения позиции точки
    def test_get_position(self):
        c1 = cells.Cell(x=1, y=2)
        c2 = cells.Cell(x=1, y=2)
        c3 = cells.Cell(x=1, y=1)
        self.assertEqual(c1.get_position(), (1, 2))
        self.assertEqual(c2.get_position(), (1, 2))
        self.assertEqual(c3.get_position(), (1, 1))

class TestCellA(unittest.TestCase):
    # Тест совпадения "==" двух клеток
    def test___eq__(self):
        c1 = cells.CellA(x=1, y=2)
        c2 = cells.CellA(x=1, y=2)
        c3 = cells.CellA(x=1, y=1)
        self.assertTrue(c1 == c2)
        self.assertFalse(c2 == c3)
        self.assertFalse(c1 == c3)

    # Тест получения позиции точки
    def test_get_position(self):
        c1 = cells.CellA(x=1, y=2)
        c2 = cells.CellA(x=1, y=2)
        c3 = cells.CellA(x=1, y=1)
        self.assertEqual(c1.get_position(), (1, 2))
        self.assertEqual(c2.get_position(), (1, 2))
        self.assertEqual(c3.get_position(), (1, 1))



if __name__ == '__main__':
    unittest.main()