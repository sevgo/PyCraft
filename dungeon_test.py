import unittest
from dungeon import Dungeon
import os


class dungeon_test(unittest.TestCase):
    def setUp(self):
        self.dungeon_map = [
            ['S', '.', '#', '#', '.', '.', '.', '.', '.', 'T'],
            ['#', 'T', '#', '#', '.', '.', '#', '#', '#', '.'],
            ['#', '.', '#', '#', '#', 'E', '#', '#', '#', 'E'],
            ['#', '.', 'E', '.', '.', '.', '#', '#', '#', '.'],
            ['#', '#', '#', 'T', '#', '#', '#', '#', '#', 'G']]
        f = open('test_level.txt', 'w')
        for line in self.dungeon_map:
            f.write(''.join(line) + '\n')
        f.close()
        self.dungeon = Dungeon("test_level.txt")

    def tearDown(self):
        os.remove("test_level.txt")

    def test_init(self):
        self.assertEqual(self.dungeon.dungeon_map, self.dungeon_map)

    def test_find_item_coordinates(self):
        self.assertEqual(self.dungeon._find_item_coordinates('S'), (0, 0))
        self.assertEqual(self.dungeon._find_item_coordinates('G'), (4, 9))


if __name__ == '__main__':
    unittest.main()
