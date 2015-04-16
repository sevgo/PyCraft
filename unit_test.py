#!/usr/bin/env python3
import unittest
from unit import Unit
from weapon import Weapon
from spell import Spell


class unit_test(unittest.TestCase):
    def setUp(self):
        self.unit = Unit(health=100, mana=100)

    def test_init(self):
        self.assertEqual(self.unit.health, 100)
        self.assertEqual(self.unit.mana, 100)
        self.assertEqual(self.unit._max_health, 100)
        self.assertEqual(self.unit._max_mana, 100)

    def test_get_health(self):
        self.assertEqual(self.unit.get_health(), 100)

    def test_get_mana(self):
        self.assertEqual(self.unit.get_mana(), 100)

    def test_is_alive(self):
        self.unit.health = 0
        self.assertFalse(self.unit.is_alive())

    def test_take_healing(self):
        self.unit.health = 0
        self.assertFalse(self.unit.take_healing(30))
        self.unit.health = 50
        self.unit.take_healing(100)
        self.assertEqual(self.unit.health, 100)

    def test_take_mana(self):
        self.unit.take_mana(100)
        self.assertEqual(self.unit.mana, 100)

    def test_equip_weapon(self):
        weapon = Weapon("Weapon name", 20)
        self.assertEqual(self.unit.weapon, None)
        self.unit.equip(weapon)
        self.assertEqual(self.unit.weapon, weapon)

    def test_learn_spell(self):
        spell = Spell("Spell name", 100, 50, 3)
        self.assertEqual(self.unit.spell, None)
        self.unit.learn(spell)
        self.assertEqual(self.unit.spell, spell)

    def test_attack_by_weapon(self):
        weapon = Weapon("Weapon name", 20)
        self.assertEqual(self.unit.attack(by="weapon"), 0)
        self.unit.equip(weapon)
        self.assertEqual(self.unit.attack(by="weapon"), 20)

    def test_attack_by_spell(self):
        spell = Spell("Spell name", 100, 50, 3)
        self.assertEqual(self.unit.attack(by="spell"), 0)
        self.unit.learn(spell)
        self.assertEqual(self.unit.attack(by="spell"), 100)


if __name__ == '__main__':
    unittest.main()
