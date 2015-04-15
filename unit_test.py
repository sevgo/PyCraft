#!/usr/bin/env python3
import unittest
from unit import Unit


class unit_test(unittest.TestCase):
    def setUp(self):
        self.unit = Unit(100, 100)

    def test_init(self):
        self.assertEqual(self.unit.health, 100)
        self.assertEqual(self.unit.mana, 100)

    def test_is_alive(self):
        self.unit.health = 0
        self.assertFalse(self.unit.is_alive())


if __name__ == '__main__':
    unittest.main()
