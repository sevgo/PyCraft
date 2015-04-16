import unittest
from dungeon import Dungeon
import os


class dungeon_test(unittest.TestCase):
    def setUp(self):
        self.dungeon_map = [['#', '#'], ['#', '#']]
        f = open('test_level.txt', 'w')
        for line in self.dungeon_map:
            f.write(''.join(line) + '\n')
        f.close()
        self.dungeon = Dungeon("test_level.txt")

    def tearDown(self):
        os.remove("test_level.txt")

    def test_init(self):
        self.assertEqual(self.dungeon.dungeon_map, self.dungeon_map)


if __name__ == '__main__':
    unittest.main()