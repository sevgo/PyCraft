#!/usr/bin/env python3

from treasure import Treasure
import unittest
from weapon import Weapon
from spell import Spell

class Test_Treasure(unittest.TestCase):

    def test_get_weapon(self):
       t = Treasure()
       self.assertIsInstance(t.get_weapon(), Weapon)
       self.assertIsInstance(t.get_spell(), Spell)
       weapon = t.get_spell()
       self.assertNotEqual(weapon.name, 'axe')


if __name__ == "__main__":
    unittest.main()
