#!/usr/bin/env python3

from treasure import Treasure
import unittest
from weapon import Weapon
from spell import Spell

class Test_Treasure(unittest.TestCase):

    def setUp(self):
        self.t = Treasure.load_treasures("test.json")

    def test_is_treasure(self):
        self.assertIsInstance(self.t, Treasure)

    def test_get_weapon(self):
        self.assertIsInstance(self.t._get_random_weapon(), Weapon)
        weapon = self.t._get_random_spell()
        self.assertNotEqual(weapon.name, 'axe')
        self.assertNotEqual(weapon.name, 'pike')
        self.assertNotEqual(weapon.name, 'sword')

    def test_get_spell(self):
        self.assertIsInstance(self.t._get_random_spell(), Spell)
        self.assertIsInstance(self.t._get_random_spell().name, str)

if __name__ == "__main__":
    unittest.main()
