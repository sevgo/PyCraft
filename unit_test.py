#!/usr/bin/env python3
import unittest
from unit import Unit


class unit_test(unittest.TestCase):
    def setUp(self):
        self.unit = Unit(health=100, mana=100)

    def test_init(self):
        self.assertEqual(self.unit.health, 100)
        self.assertEqual(self.unit.mana, 100)

    def test_get_health(self):
        self.assertEqual(self.unit.get_health(), 100)

    def test_get_mana(self):
        self.assertEqual(self.unit.get_mana(), 100)

    def test_is_alive(self):
        self.unit.health = 0
        self.assertFalse(self.unit.is_alive())

    def test_healing(self):
        self.unit.health = 0
        self.assertFalse(self.unit.take_healing(30))
        self.unit.health = 50
        self.unit.take_healing(100)
        self.assertEqual(self.unit.health, 100)

    def test_take_mana(self):
        self.unit.take_mana(100)
        self.assertEqual(self.unit.mana, 100)


if __name__ == '__main__':
    unittest.main()
