#!/usr/bin/env python3
from hero import Hero
import unittest


class Test_Hero(unittest.TestCase):
    def setUp(self):
        self.barny = Hero("Barny", "PyMag", 100, 100, 5)

    def test_Born_Hero(self):
        self.assertIsInstance(self.barny, Hero)
        self.assertEqual(self.barny.mana, 100)
        self.assertEqual(self.barny.health, 100)
        self.assertEqual(self.barny.name, "Barny")
        self.assertEqual(self.barny.title, "PyMag")

    # def test_Get_Health(self):
    #     self.assertEqual(self.barny.get_health(), 100)

    def test_Known_As(self):
        self.assertEqual(self.barny.known_as(), "Barny the PyMag")

if __name__ == "__main__":
    unittest.main()
