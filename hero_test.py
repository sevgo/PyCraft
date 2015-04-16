#!/usr/bin/env python3
from hero import Hero
import unittest

class Test_Hero(unittest.TestCase):
    def stUp(self):
        barny = Hero(name="Barny", title="PyMag", health=100, mana=100,
                     mana_regeneration_rate=5)


    def Test_Born_Hero(self):
        self.assertIsInstance(self.barny, Hero)
        self.assertEqual(self.barny.mana, 100)

    def Test_Get_Health(self):
        self.assertEqual(self.barny.get_health(), 100)

    def Test_Known_As(self):
        self.assertEqual(self.barny.known_as(), "Barny the PyMag")

if __name__ == "__main__":
    unittest.main()
