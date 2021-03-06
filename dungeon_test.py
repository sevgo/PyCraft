import unittest
from dungeon import Dungeon
from unit import Unit
from spell import Spell
from fight import Fight
import os


class dungeon_test(unittest.TestCase):
    def setUp(self):
        self.dungeon_map = [
            ['.', 'S', '#', '#', '.', '.', '.', '.', '.', 'T'],
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
        self.assertEqual(self.dungeon._find_item_coordinates('S'), (0, 1))
        self.assertEqual(self.dungeon._find_item_coordinates('G'), (4, 9))

    def test_spawn(self):
        hero = Unit(100, 100, 5)
        self.dungeon.spawn(hero)
        self.assertEqual(self.dungeon.dungeon_map[0][1], 'H')

    def test_prin_map(self):
        map_string = """.S##.....T
#T##..###.
#.###E###E
#.E...###.
###T#####G"""
        self.assertEqual(self.dungeon.print_map(), map_string)

    def test_move_hero(self):
        hero = Unit(100, 100, 5)
        self.dungeon.spawn(hero)
        self.assertFalse(self.dungeon.move_hero('up'))
        self.assertTrue(self.dungeon.move_hero('left'))
        # self.assertTrue(self.dungeon.move_hero('rigth'))
        self.assertTrue(self.dungeon.move_hero('rigth'))
        self.assertTrue(self.dungeon.move_hero('down'))
        self.assertTrue(self.dungeon.move_hero('down'))
        self.assertEqual(self.dungeon.hero_possition, (2, 1))
        self.assertEqual(self.dungeon.dungeon_map[1][1], '.')
        self.dungeon_map[0][1] = '.'
        self.dungeon_map[1][1] = '.'
        self.dungeon_map[2][1] = 'H'
        self.assertEqual(self.dungeon.dungeon_map, self.dungeon_map)

    def test_found_treasure(self):
        hero = Unit(100, 100, 5)
        hero.health = 1
        hero.mana = 1
        self.dungeon.spawn(hero)
        self.dungeon._found_treasure('mana')
        self.assertGreater(hero.mana, 1)
        self.dungeon._found_treasure('health')
        self.assertGreater(hero.health, 1)
        self.dungeon._found_treasure('weapon')
        self.assertNotEqual(hero.weapon, None)
        self.dungeon._found_treasure('spell')
        self.assertNotEqual(hero.spell, None)

    def test_create_enemy(self):
        enemy = self.dungeon._create_enemy(100, 100, 100)
        self.assertEqual(enemy.health, 100)
        self.assertEqual(enemy.mana, 100)
        self.assertEqual(enemy.damage, 100)

    def test_find_enemy(self):
        self.dungeon.hero_possition = (3, 3)
        self.dungeon.dungeon_map[3][3] = 'H'

    def test_hero_attack(self):
        hero = Unit(100, 100, 5)
        hero.learn(Spell('a', 10, 10, 2))
        self.dungeon.spawn(hero)
        self.dungeon.move_hero('down')
        self.dungeon.move_hero('down')
        self.assertEqual('Nothing in casting range 2',
                         self.dungeon.hero_attack(by="spell"))
        self.dungeon.move_hero('down')
        self.assertIsInstance(self.dungeon.hero_attack(by='spell'), Fight)

if __name__ == '__main__':
    unittest.main()
