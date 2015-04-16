#!/usr/bin/env python3

from unit import Unit
from enemy import Enemy
import unittest


class Test_Enemy(unittest.TestCase):
    def setUp(self):
        henry = Enemy(health=70, mana=45, damage=20)

    def Test_Enemy_Born(self):
        self.assertIsInstance(self.henry, Enemy)
        self.assertTrue(self.henry.mana == 45)
        self.assertEqual(self.henry.mana_regeneration_rate, 0)


if __name__ == "__main__":
    unittest.main()
