#!/usr/bin/env python3
import unittest
from unit import Unit
from weapon import Weapon
from spell import Spell


class unit_test(unittest.TestCase):
    def setUp(self):
        self.unit = Unit(health=100, mana=100, mana_regeneration_rate=5)

    def test_init(self):
        self.assertEqual(self.unit.health, 100)
        self.assertEqual(self.unit.mana, 100)
        self.assertEqual(self.unit._max_health, 100)
        self.assertEqual(self.unit._max_mana, 100)
        self.assertEqual(self.unit.mana_regeneration, 5)

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
        self.unit.take_healing(-50)
        self.assertEqual(self.unit.get_health(), 100)

    def test_take_mana(self):
        self.unit.mana = 0
        self.unit.take_mana(moved=True)
        self.assertEqual(self.unit.mana, 5)
        self.unit.take_mana(120)
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

    def test_attack_without_weapon_or_spell(self):
        self.assertEqual(self.unit.attack(), 0)

    def test_attack_with_better_weapon(self):
        spell = Spell("S", 10, 20, 5)
        weapon = Weapon('W', 50)
        self.unit.learn(spell)
        self.unit.equip(weapon)
        self.assertEqual(self.unit.attack(), 50)

    def test_attack_with_equal_weapon_and_spell(self):
        spell = Spell("S", 50, 50, 5)
        weapon = Weapon('W', 50)
        self.unit.learn(spell)
        self.unit.equip(weapon)
        self.assertEqual(self.unit.attack(), 50)
        self.assertEqual(self.unit.mana, 50)

    def test_cant_attack_with_weapon_from_distance(self):
        weapon = Weapon('W', 50)
        self.unit.equip(weapon)
        # self.assertEqual(self.unit.attack(distance=2), 0)
        self.assertEqual(self.unit.attack(), 0)

    def test_attack_by_weapon(self):
        weapon = Weapon("Weapon name", 20)
        self.assertEqual(self.unit.attack(by="weapon"), 0)
        self.unit.equip(weapon)
        self.assertEqual(self.unit.attack(by="weapon"), 20)

    def test_attack_by_spell(self):
        spell = Spell("Spell name", 100, 50, 3)
        self.assertEqual(self.unit.attack(by="spell"), 0)
        self.unit.learn(spell)
        # self.assertEqual(self.unit.attack(by="spell"), 100)

    def test_take_damage(self):
        self.unit.take_damage(20)
        self.assertEqual(self.unit.health, 80)
        self.unit.take_damage(90)
        self.assertEqual(self.unit.health, 0)

    def test_can_cast(self):
        # self.assertFalse(self.unit.can_cast())
        self.unit.learn(Spell('a', 10, 10, 3))
        # self.assertTrue(self.unit.can_cast(1))
        # self.assertTrue(self.unit.can_cast(3))
        # self.assertFalse(self.unit.can_cast(4))
        self.assertTrue(self.unit.can_cast())
        self.unit.mana = 5
        # self.assertFalse(self.unit.can_cast(1))
        self.assertFalse(self.unit.can_cast())


if __name__ == '__main__':
    unittest.main()
